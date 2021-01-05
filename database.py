# engine = sqlalchemy.create_engine(DATABASE_URL)

import databases
import sqlalchemy
from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route


# Configuration from environment variables or '.env' file.
config = Config(".env")
DATABASE_URL = config("DATABASE_URL")
metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)


on_startup = [
    database.connect,
]

on_shutdown = [
    database.disconnect,
]