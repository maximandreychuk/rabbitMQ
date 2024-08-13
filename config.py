import logging
import pika

RMQ_HOST = '0.0.0.0'
RMQ_PORT = '5672'
RMQ_USER = 'quest'
RMQ_PASSWORD = 'quest'
MQ_EXCHANGE = ""
MQ_ROUTING_KEY = "hello"

connection_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD)

)


def get_connection() -> pika.BlockingConnection:
    return pika.BlockingConnection(
        parameters=connection_params
    )


def configure_logging(level: int = logging.INFO):
    logging.basicConfig(level=level,
                        filename='logging.log',
                        format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                        datefmt='%H:%M:%S',
                        )
