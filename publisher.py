import logging
from typing import TYPE_CHECKING
from random import randint
import time

from config import (
    get_connection,
    configure_logging,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY
)

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

log = logging.getLogger(__name__)


def produce_message(channel: "BlockingChannel"):
    while True:
        queue = channel.queue_declare(queue=MQ_ROUTING_KEY)
        log.info(f"Declared queue {MQ_ROUTING_KEY}, {queue}")
        message_body = f"This is my number {randint(1, 100)}"
        log.debug(f"Publish message {message_body}")
        channel.basic_publish(
            exchange=MQ_EXCHANGE,
            routing_key=MQ_ROUTING_KEY,
            body=message_body
        )
        log.warning(f"Published message {message_body}")
        time.sleep(randint(4, 10))


def main():
    configure_logging(level=logging.INFO)
    with get_connection() as connection:
        log.info(f"Created connection {connection}")
        with connection.channel() as channel:
            log.info(f"Created channel {channel}")
            produce_message(channel=channel)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning('Bye')
