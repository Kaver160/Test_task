from sqlalchemy.ext.asyncio import  async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from src.config import settings

DATABASE_URL = settings.database_url
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
