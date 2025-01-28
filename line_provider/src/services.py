from .repositories import EventRepository
from src.shemas import EventStatus
from src.queue import send_update_message


class EventService:
    def __init__(self, repository: EventRepository):
        self.repository = repository

    async def get_events(self):
        return await self.repository.get_events()

    async def create_event(self, event):
        await self.repository.create_event(event)
        return event

    async def get_event(self, event_id: str):
        return await self.repository.get_event(event_id)

    async def update_event(self, event_id: str, status: EventStatus):
        event = await self.repository.update_event(event_id, status)
        if event:
            await send_update_message(event_id=event_id, status=status)
        return event
