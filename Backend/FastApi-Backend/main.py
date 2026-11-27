from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from os import getenv
from typing import Annotated
from uuid import UUID

from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from fastapi.concurrency import run_in_threadpool
from psycopg.errors import ForeignKeyViolation

from sqlalchemy import func
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, col, create_engine, select
from models.ApplicationModels.MessagesIn import (
    CustomerUserIn,
    CustomerUserResponse,
    MessageAccepted,
    MessageIn,
)
from models.db.customer_session import CustomerSession
from models.db.customer_user import CustomerUser
from models.db.thread import Thread
from utils.customer_session import (
    CUSTOMER_SESSION_COOKIE,
    require_thread_session,
    set_customer_session_cookie,
)
from utils.database import get_session
import boto3


sqs = boto3.client("sqs")


def check_database_connection(engine: Engine) -> None:
    with engine.connect() as connection:
        connection.exec_driver_sql("SELECT 1")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    database_url = getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("Set DATABASE_URL before starting FastAPI.")

    engine = create_engine(database_url, pool_pre_ping=True, connect_args={"connect_timeout": 8})
    try:
        await run_in_threadpool(check_database_connection, engine)
        app.state.engine = engine
        yield
    finally:
        await run_in_threadpool(engine.dispose)


app = FastAPI(lifespan=lifespan)


# Deliberately checks nothing but the process itself: if this also checked Postgres or Redis,
# one dependency outage would make the load balancer take every instance out of service.
@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/threads/{thread_id}/messages",
    status_code=status.HTTP_202_ACCEPTED,
    dependencies=[Depends(require_thread_session, scope="function")],
)
async def post_message(thread_id: UUID, message: MessageIn) -> MessageAccepted:
    # TODO: save the message, put the agent job on SQS, then return the message ID.
    # sqs.send_message(QueueUrl="", MessageBody=)
    sqs.send_message("")
    
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented yet")



# TODO: forward this reply's Redis stream entries to the widget as server-sent events.
@app.get("/messages/{message_id}/events")
async def stream_reply(message_id: UUID) -> None:
    
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "Not implemented yet")





# endpoint that creates a customer_user, which is any person on the internet who wants to reach customer support service for a particular organization. If the organization does not exist, the customer wont be able to talk to anybody. 
@app.post(
    "/customer_users/",
    status_code=status.HTTP_201_CREATED,
    responses={status.HTTP_200_OK: {"model": CustomerUserResponse}},
)
def create_customer_user(
    body: CustomerUserIn,
    request: Request,
    response: Response,
    session: Annotated[Session, Depends(get_session)],
) -> CustomerUserResponse:
    # Serialize lookups and inserts for the same organization and email until commit.
    lock_key = f"customer_user:{body.organization_id}:{body.email}"
    session.exec(select(func.pg_advisory_xact_lock(func.hashtextextended(lock_key, 0)))).one()

    customer = session.exec(
        select(CustomerUser)
        .where(CustomerUser.organization_id == body.organization_id, CustomerUser.email == body.email)
        .order_by(CustomerUser.id)
        .limit(1)
    ).first()
    thread = None
    
    
    
    if customer is not None:
        token = request.cookies.get(CUSTOMER_SESSION_COOKIE)
        if not token or session.exec(
            select(CustomerSession.id).where(
                CustomerSession.id == CustomerSession.hash_token(token),
                CustomerSession.customer_user_id == customer.id,
                CustomerSession.expires_at > func.clock_timestamp(),
            )
        ).first() is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Email verification required")

        thread = session.exec(
            select(Thread)
            .where(Thread.customer_user_id == customer.id)
            .order_by(col(Thread.created_at).desc(), col(Thread.id).desc())
            .limit(1)
        ).first()
        response.status_code = status.HTTP_200_OK

    new_token = None
    try:
        if customer is None:
            customer = CustomerUser(**body.model_dump())
            session.add(customer)
            session.flush()
            customer_session, new_token = CustomerSession.issue(customer.id)
            session.add(customer_session)

        if thread is None:
            thread = Thread(customer_user_id=customer.id)
            session.add(thread)

        customer_response = CustomerUserResponse(
            id=customer.id,
            organization_id=customer.organization_id,
            email=customer.email,
            name=customer.name,
            thread_id=thread.id,
        )
        session.commit()
    except IntegrityError as error:
        session.rollback()
        if isinstance(error.orig, ForeignKeyViolation):
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Organization not found") from error
        raise

    if new_token is not None:
        set_customer_session_cookie(request, response, new_token)

    return customer_response
