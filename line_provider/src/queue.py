import aio_pika
from aio_pika import exceptions
import logging
from src.shemas import EventStatus
from src.config import settings
logger = logging.getLogger(__name__)


async def send_update_message(event_id: str, status: EventStatus):
    try:
        connection = await aio_pika.connect_robust(settings.rabbitmq_url)
        async with connection:
            channel: aio_pika.abc.AbstractChannel = await connection.channel()
            exchange = await channel.declare_exchange(
                settings.RABBITMQ_EXCHANGE,
                aio_pika.ExchangeType.FANOUT)
            message = aio_pika.Message(
                body=f"{event_id},{status.value}".encode())
            await exchange.publish(message, routing_key="")
            logger.info("message successfully published")
    except exceptions.CONNECTION_EXCEPTIONS as e:
        logger.error(e)
