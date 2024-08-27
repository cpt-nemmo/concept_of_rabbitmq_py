from typing import TYPE_CHECKING

from config import (
    get_conn,
    MQ_ROUTING_KEY,
)


if TYPE_CHECKING:
    from pika.adapters.blocking_connection import BlockingChannel
    from pika.spec import Basic, BasicProperties


def process_new_message(
        channel: "BlockingChannel",
        method: "Basic.Deliver",
        properties: "BasicProperties",
        body: bytes
) -> None:
    print("Channel: ", channel)
    print("Method: ", method)
    print("Properties: ", properties)
    print("Body: ", body)
    channel.basic_ack(delivery_tag=method.delivery_tag)


def consume_messages(channel: "BlockingChannel") -> None:
    channel.basic_consume(
        queue=MQ_ROUTING_KEY,
        on_message_callback=process_new_message,
    )
    print("Waiting for messages.")
    channel.start_consuming()


def main():
    with get_conn() as conn:
        print("Conn has been created")
        with conn.channel() as channel:
            print("Channel has been created")
            consume_messages(channel)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
