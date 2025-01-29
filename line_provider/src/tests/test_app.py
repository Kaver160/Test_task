import pytest
from httpx import AsyncClient, ASGITransport
from dotenv import load_dotenv

load_dotenv()
from src.main import app


@pytest.fixture(scope="function")
async def async_client():
    async with AsyncClient(transport=ASGITransport(app=app),
                           base_url="http://test") as ac:
        yield ac


@pytest.mark.asyncio
async def test_get_events(async_client):
    response = await async_client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.asyncio
async def test_create_event(async_client):
    event_data = {
        "id": "4",
        "coefficient": '1.45',
        "deadline": "2025-02-20T00:00:00",
        "status": "unfinished"
    }
    response = await async_client.post("/events", json=event_data)
    assert response.status_code == 201
    json_response = response.json()
    assert json_response["id"] == event_data["id"]
    assert json_response["coefficient"] == event_data["coefficient"]


@pytest.mark.asyncio
async def test_update_event(async_client):
    update_data = {"status": "team1_won"}
    response = await async_client.put("/events/1", json=update_data)
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["status"] == update_data["status"]