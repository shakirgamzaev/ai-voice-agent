from datetime import datetime
from typing import Literal
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, DateTime, Text, func
from sqlmodel import Field, SQLModel

from models.db.thread import Thread


class Message(SQLModel, table=True):
    __tablename__ = "messages"
    __table_args__ = (
        CheckConstraint("role IN ('user', 'assistant')", name="ck_messages_role"),
        {"schema": "public"},
    )

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    thread_id: UUID = Field(foreign_key=f"public.{Thread.__tablename__}.id", index=True)
    role: Literal["user", "assistant"] = Field(sa_type=Text)
    text: str = Field(sa_type=Text)
    created_at: datetime | None = Field(
        default=None,
        nullable=False,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
    )
    reply_to_message_id: UUID | None = Field(default=None, foreign_key="public.messages.id")
