from src.shemas import CreateEvent, EventStatus


class EventRepository:
    def __init__(self, model):
        self.model = model

    async def get_events(self):
        return self.model.events

    async def create_event(self, event: CreateEvent):
        self.model.events[event.id] = event

    async def get_event(self, event_id: str):
        return self.model.events.get(event_id)

    async def update_event(self, event_id: str, status: EventStatus):
        event = self.model.events.get(event_id)
        if event:
            event.status = status
        return event
