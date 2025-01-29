from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_db
from src.repositories.beta_repository import BetaRepository
from src.schemas import CreateBeta, EventStatus
from fastapi import Query, Depends


class BetaService:
    def __init__(self, db: AsyncSession = Depends(get_db)):
        self.bet_repository = BetaRepository(db)

    async def get_all_bets(self,
                           limit: int = Query(100, ge=0),
                           offset: int = Query(0, ge=0)):
        return await self.bet_repository.get_bets(limit, offset)

    async def create_bet(self, create_beta: CreateBeta):
        return await self.bet_repository.create_new_bet(create_beta)

    async def update_bet_status(self, event_id: str, status: EventStatus):
        return await self.bet_repository.update_bet_status(event_id, status)
