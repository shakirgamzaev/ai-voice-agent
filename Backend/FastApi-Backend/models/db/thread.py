from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, func
from sqlmodel import Field, SQLModel

from models.db.customer_user import CustomerUser


class Thread(SQLModel, table=True):
    __tablename__ = "threads"
    __table_args__ = {"schema": "public"}

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    customer_user_id: UUID = Field(
        foreign_key=f"public.{CustomerUser.__tablename__}.id",
        index=True,
    )
    created_at: datetime | None = Field(
        default=None,
        nullable=False,
        sa_type=DateTime(timezone=True),
        sa_column_kwargs={"server_default": func.now()},
    )
