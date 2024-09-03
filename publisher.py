import json
from typing import TYPE_CHECKING

from config import (
    get_conn,
    MQ_EXCHANGE,
    MQ_ROUTING_KEY,
)


if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel

data = {
    "to": "ysfedoseev@yandex.ru",
    "key": "1234"
}


def produce_message(channel: "BlockingChannel") -> None:
    queue = channel.queue_declare(queue=MQ_ROUTING_KEY)
    channel.basic_publish(
        exchange=MQ_EXCHANGE,
        routing_key=MQ_ROUTING_KEY,
        body=json.dumps(data).encode('UTF-8'),
    )


def main():
    with get_conn() as conn:
        print("Conn has been created")
        with conn.channel() as channel:
            print("Channel has been created")
            produce_message(channel)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
