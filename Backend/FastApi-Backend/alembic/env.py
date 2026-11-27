from logging.config import fileConfig
from os import getenv

from alembic import context
from alembic.autogenerate.api import AutogenContext
from sqlalchemy import create_engine, pool
from sqlalchemy.engine import make_url
from sqlalchemy.schema import SchemaItem
from sqlmodel import SQLModel
from sqlmodel.sql.sqltypes import AutoString

# Import the models to register their tables with SQLModel.
from models.db import customer_session, message  # pylint: disable=unused-import

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = SQLModel.metadata


def include_name(
    name: str | None, type_: str, _parent_names: dict[str, str | None]
) -> bool:
    return type_ != "schema" or name == "public"


def include_object(
    _object: SchemaItem,
    _name: str | None,
    type_: str,
    reflected: bool,
    compare_to: SchemaItem | None,
) -> bool:
    # Only generate changes for tables registered by FastAPI's models.
    return not (type_ == "table" and reflected and compare_to is None)


def render_item(type_: str, item: object, autogen_context: AutogenContext) -> bool:
    if type_ == "type" and isinstance(item, AutoString):
        autogen_context.imports.add("import sqlmodel")
    return False


def run_migrations_offline() -> None:
    context.configure(
        dialect_name="postgresql",
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        version_table_schema="public",
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    database_url = getenv("DATABASE_URL")
    if not database_url:
        raise RuntimeError("Set DATABASE_URL before running Alembic against PostgreSQL.")

    url = make_url(database_url)
    options = " ".join(url.normalized_query.get("options", (getenv("PGOPTIONS", ""),)))
    # Keep public explicit during reflection to match the models' foreign keys.
    connectable = create_engine(
        url,
        poolclass=pool.NullPool,
        connect_args={"options": f"{options} -csearch_path=pg_catalog,public"},
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            include_schemas=True,
            include_name=include_name,
            include_object=include_object,
            render_item=render_item,
            version_table_schema="public",
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
