import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(
    queue="badge_print_requests",
    durable=True
)

channel.basic_publish(
    exchange="",
    routing_key="badge_print_requests",
    body="Test badge print request"
)

print("Print request sent to RabbitMQ!")

connection.close()