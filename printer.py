import pika
import requests

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(
    queue="badge_print_requests",
    durable=True
)

def process_print_request(ch, method, properties, body):
    message = body.decode()

    print(f"Printer received: {message}")

    # Extract QR code from the message
    qr_code = message.replace("Print badge for ", "")

    # Simulate successful printing, then notify the kiosk
    response = requests.post(
        "http://127.0.0.1:8000/webhook/print-complete",
        json={
            "qr_code": qr_code,
            "status": "printed"
        }
    )

    print(f"Webhook response: {response.status_code}")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(
    queue="badge_print_requests",
    on_message_callback=process_print_request
)

print("Printer is waiting for print requests...")

channel.start_consuming()