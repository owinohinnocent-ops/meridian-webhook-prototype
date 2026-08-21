import json
from pathlib import Path

from fastapi import FastAPI

STATE_FILE = Path(__file__).parent / "attendees.json"

app = FastAPI()

def load_attendees():
    with open(STATE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_attendees(attendees):
    with open(STATE_FILE, "w", encoding="utf-8") as file:
        json.dump(attendees, file, indent=2)

@app.post("/webhook/print-complete")
def print_complete(data: dict):
    qr_code = data.get("qr_code")
    status = data.get("status")

    attendees = load_attendees()
    attendee = attendees.get(qr_code)

    if attendee is None:
        return {
            "success": False,
            "message": "Attendee not found",
        }

    if status == "printed":
        attendee["status"] = "CHECKED_IN"
        save_attendees(attendees)

    print(f"Print completed: {data}")

    return {
        "success": True,
        "message": "Attendee checked in",
        "qr_code": qr_code,
        "status": "CHECKED_IN",
    }