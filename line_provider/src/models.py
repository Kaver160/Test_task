from datetime import datetime, timedelta
from src.shemas import CreateEvent, EventStatus


class EventModel:
    def __init__(self):
        self.events: dict[str, CreateEvent] = {
            '1': CreateEvent(id='1', coefficient=1.2,
                             deadline=datetime.now() + timedelta(days=2),
                             status=EventStatus.UNFINISHED),
            '2': CreateEvent(id='2', coefficient=1.15,
                             deadline=datetime.now() + timedelta(days=5),
                             status=EventStatus.UNFINISHED),
            '3': CreateEvent(id='3', coefficient=1.67,
                             deadline=datetime.now() + timedelta(days=7),
                             status=EventStatus.UNFINISHED)
        }
