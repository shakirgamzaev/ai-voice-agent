import asyncio

from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
from pydantic import BaseModel, Field


class MessageBody(BaseModel):
    text: str


class SqsRecord(BaseModel):
    body: str


class SqsEvent(BaseModel):
    records: list[SqsRecord] = Field(alias="Records")


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
        user_text = MessageBody.model_validate_json(record.body).text
        result = Runner.run_streamed(agent, user_text)

        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)

        print(flush=True)


def lambda_handler(event: dict[str, object], context) -> None:
    sqs_event = SqsEvent.model_validate(event)
    async_runner.run(stream_replies(sqs_event))
