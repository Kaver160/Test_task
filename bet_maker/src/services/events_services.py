from datetime import datetime

import aiohttp
from fastapi import HTTPException
from starlette import status

from src.config import settings
from src.schemas import Event


class EventsService:
    @staticmethod
    async def fetch_events_from_provider():
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(
                        f'{settings.line_provider_url}/events') as response:
                    if response.status != status.HTTP_200_OK:
                        raise HTTPException(status_code=response.status,
                                            detail="Error fetching events")
                    return await response.json()
            except aiohttp.ClientError as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"Error connecting to line-provider: {str(e)}")

    async def get_events(self):
        data = await self.fetch_events_from_provider()
        event_list = [Event.model_validate(item) for item in data.values() if
                      Event.model_validate(item).deadline.replace(
                          tzinfo=None) > datetime.now()]
        return event_list
