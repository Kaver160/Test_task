from dotenv import load_dotenv
from pathlib import Path

from pydantic_settings import BaseSettings

dotenv_path = a = Path('.') / '.env'
load_dotenv(dotenv_path=dotenv_path)


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Bet Maker'
    PROJECT_VERSION: str = '1.0.0'

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    LINE_PROVIDER_URL: str

    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: str
    RABBITMQ_EXCHANGE: str
    RABBITMQ_QUEUE: str

    @property
    def database_url(self):
        DATABASE_URL = (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}")
        return DATABASE_URL

    @property
    def line_provider_url(self):
        return self.LINE_PROVIDER_URL

    @property
    def rabbitmq_url(self):
        RABBITMQ_URL = (
            f'amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@'
            f'{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/'
        )
        return RABBITMQ_URL


settings = Settings()
