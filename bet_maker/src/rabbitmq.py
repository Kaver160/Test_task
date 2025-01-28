import asyncio

import aio_pika
import logging

from src.database import SessionLocal
from src.config import settings
from src.services.beta_services import BetaService

logger = logging.getLogger(__name__)


async def consume_messages():
    while True:
        try:
            logger.info('Attempting to connect to RabbitMQ...')
            connection = await aio_pika.connect_robust(settings.rabbitmq_url)
            async with connection:
                channel = await connection.channel()
                queue = await channel.declare_queue(settings.RABBITMQ_QUEUE,
                                                    auto_delete=True)
                exchange = await channel.declare_exchange(
                    settings.RABBITMQ_EXCHANGE,
                    aio_pika.ExchangeType.FANOUT)
                await queue.bind(exchange)

                await queue.consume(on_message)
                logger.info('Started consuming messages')

                while not channel.is_closed:
                    await asyncio.sleep(1)

        except aio_pika.exceptions.ChannelInvalidStateError:
            logger.warning('Channel is in invalid state, reconnecting...')
        except Exception as e:
            logger.error(f'Error occurred: {e}')
        finally:
            logger.info('Reconnecting in 5 seconds...')
            await asyncio.sleep(5)


async def on_message(message: aio_pika.IncomingMessage):
    async with message.process():
        event_id, status = message.body.decode().split(',')
        async with SessionLocal() as db:
            bet_service = BetaService(db)
            await bet_service.update_bet_status(event_id,
                                                status)
            logger.info(
                f'Message received and processed: {event_id},{status}')
