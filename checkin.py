import json
from pathlib import Path

import pika

STATE_FILE = Path(__file__).parent / "attendees.json"

def load_attendees():
    with open(STATE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_attendees(attendees):
    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(attendees, file, indent=2)

def send_print_request(qr_code):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )

    channel = connection.channel()

    channel.queue_declare(
        queue="badge_print_requests",
        durable=True
    )

    message = f"Print badge for {qr_code}"

    channel.basic_publish(
        exchange="",
        routing_key="badge_print_requests",
        body=message
    )

    connection.close()

def scan_attendee(qr_code):
    attendees = load_attendees()
    attendee = attendees.get(qr_code)

    if attendee is None:
        return {
            "success": False,
            "message": "Attendee not found",
        }

    if attendee["status"] == "CHECKED_IN":
        return {
            "success": False,
            "message": "Attendee has already checked in",
        }

    if attendee["status"] == "PENDING":
        return {
            "success": False,
            "message": "Badge printing is already pending",
        }

    attendee["status"] = "PENDING"
    save_attendees(attendees)

    send_print_request(qr_code)

    return {
        "success": True,
        "message": "Badge printing is pending",
        "name": attendee["name"],
        "status": "PENDING",
    }