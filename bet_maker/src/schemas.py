import decimal
import enum

from pydantic import BaseModel, Field
from datetime import datetime


class CreateBeta(BaseModel):
    event_id: str
    amount: float = Field(gt=0)


class BaseBets(BaseModel):
    id: int
    event_id: str
    amount: float
    status: str
    created_at: datetime


class Bets(BaseBets):
    pass


class EventStatus(str, enum.Enum):
    UNFINISHED = "unfinished"
    TEAM1_WON = "team1_won"
    TEAM2_WON = "team2_won"


class BetaStatus(str, enum.Enum):
    WON1 = "team1_won"
    WON2 = "team2_won"
    PENDING = "pending"


class Event(BaseModel):
    id: str
    coefficient: decimal.Decimal
    deadline: datetime
    status: str
