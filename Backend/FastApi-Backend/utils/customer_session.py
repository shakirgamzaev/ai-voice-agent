from collections.abc import Iterator
from os import getenv
from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, Request, Response, status
from sqlalchemy import func
from sqlmodel import Session, col, select, update

from models.db.customer_session import CUSTOMER_SESSION_TTL, CustomerSession
from models.db.thread import Thread
from utils.database import get_session


CUSTOMER_SESSION_COOKIE = "mira_customer_session"


def set_customer_session_cookie(request: Request, response: Response, token: str) -> None:
    response.set_cookie(
        key=CUSTOMER_SESSION_COOKIE,
        value=token,
        max_age=int(CUSTOMER_SESSION_TTL.total_seconds()),
        httponly=True,
        secure=request.url.scheme == "https" or getenv("CUSTOMER_SESSION_COOKIE_SECURE") == "true",
        samesite="lax",
    )


def require_thread_session(
    thread_id: UUID,
    request: Request,
    response: Response,
    session: Annotated[Session, Depends(get_session)],
) -> Iterator[None]:
    token = request.cookies.get(CUSTOMER_SESSION_COOKIE)
    if not token:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Valid customer session required")

    valid_session = (
        col(CustomerSession.id) == CustomerSession.hash_token(token),
        col(CustomerSession.expires_at) > func.clock_timestamp(),
    )
    # Commit the renewal only when the authorized message handler succeeds.
    with session.begin():
        renewed = session.exec(
            update(CustomerSession)
            .where(
                *valid_session,
                col(Thread.id) == thread_id,
                col(Thread.customer_user_id) == col(CustomerSession.customer_user_id),
            )
            .values(expires_at=func.clock_timestamp() + CUSTOMER_SESSION_TTL)
            .execution_options(synchronize_session=False)
        )
        if renewed.rowcount == 0:
            if session.exec(select(CustomerSession.id).where(*valid_session)).first() is None:
                raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Valid customer session required")
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Thread not found")

        set_customer_session_cookie(request, response, token)
        yield
