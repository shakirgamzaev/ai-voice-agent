from uuid import UUID, uuid4

from sqlalchemy import UniqueConstraint
from sqlmodel import Column, Field, ForeignKey, MetaData, SQLModel, Table, Text


# Better Auth manages this table. FastAPI references it through a foreign key.
_organization = Table(
    "organization",
    MetaData(),
    Column("id", Text, primary_key=True),
    schema="authentication",
)


class CustomerUser(SQLModel, table=True):
    __tablename__ = "customer_user"
    __table_args__ = (
        UniqueConstraint("organization_id", "email", name="uq_customer_user_org_email"),
        {"schema": "public"},
    )

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    organization_id: str = Field(
        sa_column=Column(Text, ForeignKey(_organization.c.id), nullable=False, index=True)
    )
    email: str = Field(max_length=254)
    name: str
