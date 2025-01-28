from fastapi import FastAPI, HTTPException
from starlette import status
from src.models import EventModel
from src.repositories import EventRepository
from src.services import EventService
from src.shemas import CreateEvent, UpdateEvent

app = FastAPI()

model = EventModel()
repository = EventRepository(model)
service = EventService(repository)


@app.get("/events", status_code=status.HTTP_200_OK)
async def get_events():
    return await service.get_events()


@app.post("/events", status_code=status.HTTP_201_CREATED)
async def create_event(event: CreateEvent):
    existing_event = await service.get_event(event.id)
    if existing_event:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Event already exists")
    return await service.create_event(event)


@app.get("/events/{event_id}", status_code=status.HTTP_200_OK)
async def get_event(event_id: str):
    event = await service.get_event(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event not found")
    return event


@app.put("/events/{event_id}", status_code=status.HTTP_200_OK)
async def update_event(event_id: str, event: UpdateEvent):
    updated_event = await service.update_event(event_id, event.status)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Event not found")
    return updated_event
