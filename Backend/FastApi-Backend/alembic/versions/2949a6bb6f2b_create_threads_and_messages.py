"""Create the threads and messages tables."""

import sqlalchemy as sa
from alembic import op


revision = "2949a6bb6f2b"
down_revision = "b8032ad7863d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "threads",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("customer_user_id", sa.Uuid(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["customer_user_id"], ["public.customer_user.id"]),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )
    op.create_index(
        "ix_public_threads_customer_user_id",
        "threads",
        ["customer_user_id"],
        schema="public",
    )
    op.create_table(
        "messages",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("thread_id", sa.Uuid(), nullable=False),
        sa.Column("role", sa.Text(), nullable=False),
        sa.Column("text", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("reply_to_message_id", sa.Uuid(), nullable=True),
        sa.CheckConstraint("role IN ('user', 'assistant')", name="ck_messages_role"),
        sa.ForeignKeyConstraint(["reply_to_message_id"], ["public.messages.id"]),
        sa.ForeignKeyConstraint(["thread_id"], ["public.threads.id"]),
        sa.PrimaryKeyConstraint("id"),
        schema="public",
    )
    op.create_index(
        "ix_public_messages_thread_id",
        "messages",
        ["thread_id"],
        schema="public",
    )


def downgrade() -> None:
    op.drop_table("messages", schema="public")
    op.drop_table("threads", schema="public")
