# Meridian Day 4 Pivot Learning Journal

21/08/2026

Honestly, today was a challenging and a tough day for me.
The Day 4 pivot required me to change the badge printing process so that it would not happen directly. The idea was that when an attendee is scanned, their status should first become PENDING. A print request should then be sent to RabbitMQ. The printer should receive that request, and after the printing is completed, it should send a message back to my FastAPI webhook. The attendee should only become CHECKED_IN after that confirmation.
I understood the idea, but putting it into practice was difficult because RabbitMQ and asynchronous processing were still new to me.

The main tools I used today were Python 3.14, RabbitMQ Server 4.3.5, Erlang, Pika, FastAPI, Uvicorn, Requests, PowerShell, VS Code and JSON.
The main files I worked with were checkin.py, printer.py, webhook.py, rabbit_test.py and attendees.json.

## What I Worked On

I started with the check-in system I already had.
My test attendees were:

QR-001 - Innocent Odhiambo
QR-002 - Janet Ngugi	
QR-003 - Stephen Letoo

The main thing I wanted to achieve was this status flow:
NOT_CHECKED_IN to PENDING then finally to CHECKED_IN

I first worked on getting RabbitMQ to communicate properly with my Python application.
I used Pika to connect Python to RabbitMQ and created a queue called badge_print_requests.
I also created rabbit_test.py just to make sure that I could actually send a message to RabbitMQ before connecting everything else.
When I eventually ran it and got: Print request sent to RabbitMQ!
I knew that Python was communicating with RabbitMQ.
I then used the RabbitMQ command line to check the queue with: rabbitmqctl list_queues
I also checked the consumers using: rabbitmqctl list_consumers
This helped me confirm that the queue existed and that the printer was actually connected to it.

## Blockers I Encountered

### RabbitMQ and Erlang Challenges

One of my first problems was getting RabbitMQ to work correctly. I initially received, ERLANG_HOME not set correctly.

I also had an Erlang cookie/authentication issue. This was confusing because I had already installed RabbitMQ Server 4.3.5 and Erlang.

I had to stop and check the RabbitMQ setup before continuing. Eventually I got RabbitMQ responding properly.

I then used PowerShell commands such as: rabbitmqctl list_queues and rabbitmqctl list_consumers to confirm that the queue and consumer were actually working.

### Understanding the printer Challenges

When I ran python printer.py ,I only saw the Printer is waiting for print requests...

At first I thought something was wrong. I later understood that this was actually the correct behaviour. The printer was a consumer and was supposed to keep waiting for a message.

After sending a request, I saw: Printer received: Print badge for QR-003

That helped me understand the producer and consumer concept much better.

### Webhook connection error

When I first connected the printer to the FastAPI webhook, I received: WinError 10061

The connection to 127.0.0.1:8000 was refused.

I initially thought my code was wrong, but I realised that I had not started the FastAPI server.

I started it using Uvicorn: python -m uvicorn webhook:app --reload

Once I saw Uvicorn running on http://127.0.0.1:8000 , I ran the printer again and got: Webhook response: 200

That confirmed that the printer and webhook were communicating.

### Sharing attendee status Challenges

Another important blocker was the attendee status.

Initially, the attendee information was stored in a Python dictionary inside checkin.py. I expected the webhook to update the same dictionary after printing.

I eventually understood that checkin.py and the FastAPI application were separate Python processes, so they did not automatically share the same Python variables.

To solve this, I used attendees.json to store the attendee status.

The status could then move from: NOT_CHECKED_IN to PENDING and finally CHECKED_IN

## Testing

I tested the system using three QR codes.

For QR-003, I ran: python -c "from checkin import scan_attendee; print(scan_attendee('QR-003'))"

The system returned: Badge printing is pending

The printer then showed: Printer received: Print badge for QR-003 and later: Webhook response: 200

I checked attendees.json and QR-003 had changed to: CHECKED_IN

I also scanned QR-003 again and got: Attendee has already checked in , which showed that duplicate check-ins were being prevented.

I repeated the process for QR-001 and QR-002. Both eventually changed to CHECKED_IN.

At the end:

QR-001 → CHECKED_IN
QR-002 → CHECKED_IN
QR-003 → CHECKED_IN

### Important Lessons Learnt

The biggest lesson for me was understanding how the different parts communicate.

I now have a better understanding of:

-RabbitMQ as the message broker.
-Pika as the Python library communicating with RabbitMQ.
-checkin.py as the part sending the print request.
-printer.py as the consumer receiving the request.
-FastAPI as the webhook application.
-Uvicorn as the server running FastAPI.
-Requests as the library used by the printer to call the webhook.
-attendees.json as shared persistent storage for this simulation.

I also learnt that when something fails, I should not immediately assume that everything is broken. I can check one part at a time: RabbitMQ, the queue, the consumer, the webhook and finally the attendee status.

## My own take

To be honest, this was difficult for me.

There were several moments when I did not know what was wrong, I kept receiving errors after errors, especially with RabbitMQ and the separate processes. I also made small mistakes while working between different PowerShell terminals.

But I kept testing and fixing one problem at a time.

When I finally saw the printer receive the request, the webhook return 200, and the attendee change to CHECKED_IN, I felt that I had actually understood something and I was really excited with a sigh of relief.

I am still new to many of these technologies, so I know I need more practice. But Day 4 showed me that I can struggle with something unfamiliar and still get it working.

The first time was tough, but with practice I know I will be somewhere.
