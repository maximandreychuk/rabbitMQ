# rabbitMQ

Очереди сообщений в RabbitMQ и взаимодействие на Python

## Запуск:

Активировать виртуальное окружение и установить зависимости:

- python -m venv venv
- python venv/bin/activate
- pip freeze requirements.txt

Собрать контейнер:

- docker compose pull
- docker compose up -d
- адрес 0.0.0.0:15672

Run:

- python consumer.py для запуска потребителя
- python publisher.py для запуска отправителя


Links:
- https://www.rabbitmq.com/docs/consumer-prefetch
- https://pika.readthedocs.io/en/stable/modules/channel.html
