from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PROJECT_NAME: str = 'Line Provider'
    # PROJECT_VERSION: str = '1.0.0'

    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: str
    RABBITMQ_EXCHANGE: str

    @property
    def rabbitmq_url(self):
        RABBITMQ_URL = (
            f'amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/'
        )
        return RABBITMQ_URL


settings = Settings()
