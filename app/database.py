from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from os import environ

def get_db_url() -> str:
    """
    Returns a database URL string constructed from environment variables.

    :return: The database URL string.
    :rtype: str
    """
    
    sql_type: str = "postgres"
    sql_host: str = environ["SQL_HOST"]
    sql_password: str = environ["SQL_PASSWORD"]
    sql_port: str = environ["SQL_PORT"]
    sql_database: str = environ["SQL_DATABASE"]
    sql_username: str = environ["SQL_USERNAME"]

    return f"{sql_type}://{sql_username}:{sql_password}@{sql_host}:{sql_port}/{sql_database}"


async def init_db():
    """
    Initializes the Tortoise ORM and creates the database tables defined by the models.

    :return: None
    """
    # Initialize Tortoise ORM
    await Tortoise.init(
        db_url= get_db_url(),
        modules={
            'models': [
                'app.models.event',
                'app.models.goal',
                'app.models.image',
                'app.models.journal_entry',
                'app.models.location',
                'app.models.revision',
            ]
        }
    )

    # Create the database tables
    await Tortoise.generate_schemas()


def register_tortoise_helper(app):
    """
    Registers the FastAPI app with Tortoise ORM and creates a connection pool.

    :param app: The FastAPI app to register with Tortoise.
    :type app: FastAPI
    :return: None
    """
    
    # register the app with tortoise, this creates a connection pool
    register_tortoise(
        app,
        db_url= get_db_url(),
        modules={
            'models': [
                'app.models.event',
                'app.models.goal',
                'app.models.image',
                'app.models.journal_entry',
                'app.models.location',
                'app.models.revision',
            ]
        },
    )

# Run this to instantiate database
# import asyncpg    
# asyncio.run(init_db())


