from datetime import UTC, datetime, timedelta
from hashlib import sha512
from secrets import token_hex
from typing import Self
from uuid import UUID

from sqlalchemy import CheckConstraint, DateTime, LargeBinary
from sqlmodel import Field, SQLModel

from models.db.customer_user import CustomerUser


CUSTOMER_SESSION_TTL = timedelta(hours=12)
SESSION_TOKEN_BYTES = 64


class CustomerSession(SQLModel, table=True):
    __tablename__ = "customer_sessions"
    __table_args__ = (
        CheckConstraint("octet_length(id) = 64", name="ck_customer_sessions_id_length"),
        {"schema": "public"},
    )

    id: bytes = Field(primary_key=True, sa_type=LargeBinary)
    customer_user_id: UUID = Field(
        foreign_key=f"public.{CustomerUser.__tablename__}.id",
        index=True,
    )
    expires_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC) + CUSTOMER_SESSION_TTL,
        sa_type=DateTime(timezone=True),
    )

    @staticmethod
    def hash_token(token: str) -> bytes:
        return sha512(token.encode()).digest()

    @classmethod
    def issue(cls, customer_user_id: UUID) -> tuple[Self, str]:
        """Create a session and return its token for the cookie."""
        token = token_hex(SESSION_TOKEN_BYTES)
        return cls(id=cls.hash_token(token), customer_user_id=customer_user_id), token
