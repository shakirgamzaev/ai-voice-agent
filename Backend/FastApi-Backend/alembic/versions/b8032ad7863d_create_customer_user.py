"""Create the customer_user table for widget visitors."""

import sqlalchemy as sa
from alembic import op


revision = "b8032ad7863d"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "customer_user",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("organization_id", sa.Text(), nullable=False),
        sa.Column("email", sa.String(length=254), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["organization_id"], ["authentication.organization.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("organization_id", "email", name="uq_customer_user_org_email"),
        schema="public",
    )
    op.create_index(
        "ix_public_customer_user_organization_id",
        "customer_user",
        ["organization_id"],
        schema="public",
    )


def downgrade() -> None:
    op.drop_table("customer_user", schema="public")
