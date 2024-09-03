import pika

RMQ_HOST = 'localhost'
RMQ_PORT = 5672
RMQ_USER = 'guest'
RMQ_PASSWORD = 'guest'
MQ_EXCHANGE = ''
MQ_ROUTING_KEY = 'Hello'

conn_params = pika.ConnectionParameters(
    host=RMQ_HOST,
    port=RMQ_PORT,
    credentials=pika.PlainCredentials(RMQ_USER, RMQ_PASSWORD),
)


def get_conn() -> pika.BlockingConnection:
    return pika.BlockingConnection(conn_params)
