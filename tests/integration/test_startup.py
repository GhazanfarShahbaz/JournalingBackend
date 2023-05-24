import pytest

from app.main import app
from tests.fixtures import client


@pytest.mark.asyncio
async def test_startup_event(client):
    """
    GIVEN a FastAPI application is started
    WHEN a GET request is made to the root endpoint
    THEN the startup event will run and response status code should be 200
    AND the response body should be {"Hello": "World"}
    """
    
    # Send a GET request to the root endpoint using the TestClient
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}