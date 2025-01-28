from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.models import Beta
from src.schemas import CreateBeta, EventStatus, BetaStatus


class BetaRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_bets(self, limit: int, offset: int):
        result = await self.db.execute(select(Beta).offset(offset).limit(limit))
        return result.scalars().all()

    async def create_new_bet(self, create_beta: CreateBeta):
        db_bet = Beta(**create_beta.dict())
        self.db.add(db_bet)
        await self.db.commit()
        await self.db.refresh(db_bet)
        return db_bet

    async def update_bet_status(self, event_id: str, status: EventStatus):
        result = await self.db.execute(
            select(Beta).filter(Beta.event_id == event_id))
        bets = result.scalars().all()

        for bet in bets:
            if status == EventStatus.TEAM1_WON:
                bet.status = BetaStatus.WON1
            elif status == EventStatus.TEAM2_WON:
                bet.status = BetaStatus.WON2
            elif status == EventStatus.UNFINISHED:
                bet.status = BetaStatus.PENDING

        await self.db.commit()
