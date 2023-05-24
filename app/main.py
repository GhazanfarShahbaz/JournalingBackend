"""
This module contains the main application for running a FastAPI server.

The `app` object is an instance of the FastAPI class and is used to define and register HTTP endpoints. The default endpoint returns a simple JSON response.
"""

from fastapi import FastAPI

from app.database import register_tortoise_helper
from app.settings.generate_env import load_environment

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """
    Initializes environment variables and the Tortoise app and registers it with the FastAPI app on startup.

    :return: None
    """
    # Initialize the Tortoise app
    load_environment()
    register_tortoise_helper(app)


@app.get("/")
def read_root():
    return {"Hello": "World"}
