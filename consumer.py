import logging
from typing import TYPE_CHECKING
from random import randint

from config import (
    get_connection,
    configure_logging,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY
)

if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic, BasicProperties

log = logging.getLogger(__name__)


def process_new_message(
    ch: "BlockingChannel",
    method: "Basic.Deliver",
    properties: "BasicProperties",
    body: bytes
):
    log.warning(f"Finish processing messages {body}")


def consume_message(channel: "BlockingChannel") -> None:
    channel.basic_consume(
        queue=MQ_ROUTING_KEY,
        on_message_callback=process_new_message,
        auto_ack=True
    )
    log.warning(f"Waiting for messages")
    channel.start_consuming()


def main():
    configure_logging(level=logging.WARNING)
    with get_connection() as connection:
        log.info(f"Created connection {connection}")
        with connection.channel() as channel:
            log.info(f"Created channel {channel}")
            consume_message(channel=channel)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.warning('Bye')
