import sys
import pytest

from dotenv import load_dotenv
from os import environ

def pytest_configure():
    """
    Load environment variables and add the app directory to the sys.path.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Add the app directory to the sys.path
    root_dir: str = environ["PATH_TO_HOME_DIRECTORY"]
    sys.path.append(root_dir)

    # Load the environment configuration
    from app.settings.generate_env import load_environment
    load_environment()

pytest_plugins = ["fixtures"]
