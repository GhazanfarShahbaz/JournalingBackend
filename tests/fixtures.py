import pytest

from app.main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def client():
    """
    Create a TestClient instance for the FastAPI app for use in integration tests.
    """
    with TestClient(app) as client:
        yield client