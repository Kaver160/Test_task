import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.database import get_db
from src.rabbitmq import consume_messages
from src.schemas import CreateBeta, Bets, Event
from src.services.beta_services import BetaService
from src.services.events_services import EventsService


@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(consume_messages())
    yield
    task.cancel()


app = FastAPI(lifespan=lifespan)


@app.get("/events", response_model=list[Event])
async def get_events(
        service: EventsService = Depends(EventsService)):
    return await service.get_events()


@app.post("/beta", status_code=status.HTTP_201_CREATED)
async def create_beta(beta: CreateBeta,
                      service: BetaService = Depends(BetaService)):
    return await service.create_bet(beta)


@app.get("/bets", response_model=list[Bets])
async def get_all_bets(
        service: BetaService = Depends(BetaService),
        limit: int = Query(10, ge=0),
        offset: int = Query(0, ge=0)):
    return await service.get_all_bets(offset=offset, limit=limit)
