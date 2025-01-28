from pydantic import BaseModel, field_validator
from typing import Optional
import decimal
import enum
from datetime import datetime


class EventStatus(str, enum.Enum):
    UNFINISHED = "unfinished"
    TEAM1_WON = "team1_won"
    TEAM2_WON = "team2_won"


class EventBase(BaseModel):
    coefficient: decimal.Decimal
    deadline: datetime
    status: Optional[EventStatus] = EventStatus.UNFINISHED

    @field_validator('coefficient')
    @classmethod
    def check_decimal_places(cls, value: decimal.Decimal):
        if value.as_tuple().exponent < -2:
            raise ValueError('coefficient must have at most 2 decimal places')
        return value


class ListEvent(BaseModel):
    list_event: list[EventBase]


class CreateEvent(EventBase):
    id: str


class UpdateEvent(BaseModel):
    status: EventStatus

