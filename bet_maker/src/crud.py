from fastapi import Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Beta
from src.schemas import CreateBeta, EventStatus, BetaStatus


async def get_bets(db: AsyncSession,
                   limit: int = Query(100, ge=0),
                   offset: int = Query(0, ge=0)
                   ):
    result = await db.execute(select(Beta).offset(offset).limit(limit))
    return result.scalars().all()


async def create_new_beta(db: AsyncSession,
                          beta: CreateBeta):
    db_beta = Beta(**beta.dict())
    db.add(db_beta)
    await db.commit()
    await db.refresh(db_beta)
    return db_beta


async def update_bet_status(event_id: str,
                            status: EventStatus,
                            db: AsyncSession):
    result = await db.execute(select(Beta).filter(Beta.event_id == event_id))
    bets = result.scalars().all()

    for bet in bets:
        if status == EventStatus.TEAM1_WON:
            bet.status = BetaStatus.WON1
        elif status == EventStatus.TEAM2_WON:
            bet.status = BetaStatus.WON2
        elif status == EventStatus.UNFINISHED:
            bet.status = BetaStatus.PENDING

    await db.commit()

