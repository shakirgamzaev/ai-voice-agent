import asyncio
import json
import os
from typing import TYPE_CHECKING

import boto3
from agents import Agent, Runner, set_default_openai_key
from openai.types.responses import ResponseTextDeltaEvent
from pydantic import BaseModel, Field, field_validator

if TYPE_CHECKING:
    from mypy_boto3_secretsmanager import SecretsManagerClient

class MessageBody(BaseModel):
    text: str = Field(pattern=r"\S")

class SqsRecord(BaseModel):
    body: MessageBody

    @field_validator("body", mode="before")
    @classmethod
    def parse_body(cls, body: object) -> MessageBody:
        if not isinstance(body, str):
            raise ValueError("SQS record body must be a string")
        if body.lstrip().startswith("{"):
            return MessageBody.model_validate_json(body)
        return MessageBody(text=body)

class SqsEvent(BaseModel):
    records: list[SqsRecord] = Field(alias="Records")


secret_name = os.getenv("OPENAI_API_KEY")
if not secret_name:
    try:
        print("fetching from secrets manager")
        secrets_client: SecretsManagerClient = boto3.client("secretsmanager")
        secret = secrets_client.get_secret_value(SecretId="openai_api_key")
        api_key = json.loads(secret["SecretString"])["openai_api_key"]
        set_default_openai_key(api_key)
    except Exception as e:
        print(e)
        raise e



# Reuse the event loop and the SDK's HTTP connections across warm invocations.
async_runner = asyncio.Runner()


async def stream_replies(sqs_event: SqsEvent) -> None:
    agent = Agent(
        name="conversation agent",
        instructions=(
            "a user will ask you questions about the e commerce website. the refund policy "
            "is only in the first week. User can also ask history questions. So you are "
            "allowed to answer either history questions or question about refund policy. "
            'Anything else asked by the user should be repsonded with "Sorry can\'t help '
            'you with that. Anything else i can help you with? "'
        ),
        model="gpt-6.2-sol",
    )

    for record in sqs_event.records:
        result = Runner.run_streamed(agent, record.body.text)

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)

        print(flush=True)


def lambda_handler(event: dict[str, object], context: object) -> None:
    sqs_event = SqsEvent.model_validate(event)
    # Lambda deletes the SQS records only after this handler returns successfully.
    async_runner.run(stream_replies(sqs_event))
    
