"""Create the customer_sessions table for the widget."""

import sqlalchemy as sa
from alembic import op


revision = "70c8a0ccc151"
down_revision = "2949a6bb6f2b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "customer_sessions",
        sa.Column("id", sa.LargeBinary(), nullable=False),
        sa.Column("customer_user_id", sa.Uuid(), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=False),
        sa.CheckConstraint("octet_length(id) = 64", name="ck_customer_sessions_id_length"),
        sa.ForeignKeyConstraint(["customer_user_id"], ["public.customer_user.id"]),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )
    op.create_index(
        "ix_public_customer_sessions_customer_user_id",
        "customer_sessions",
        ["customer_user_id"],
        schema="public",
    )


def downgrade() -> None:
    op.drop_table("customer_sessions", schema="public")
