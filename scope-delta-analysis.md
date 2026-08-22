# Meridian Pivot - Scope Delta Analysis

## Project

Meridian Pivot Simulation

## Client

Solstice Events Co.

## Purpose

This document explains the scope and architecture changes caused by the Day 4 client pivot. It compares the original synchronous check-in approach with the new asynchronous solution and documents what was dropped, modified, added, and reprioritized.

## Original Scope

Before the pivot, the check-in service was expected to communicate with the badge-printer vendor synchronously.

The original workflow was:
QR Scan to  Synchronous Printer REST API to Wait for Print Success then finally to CHECKED_IN

The application would call the printer API directly and wait for the print job to succeed before marking the attendee as checked in.

The original design also required duplicate-scan protection so that an attendee who was already checked in would not receive another badge.

## Pivot Requirement

The client announced that the synchronous badge-printer API was being deprecated with no extension to the deadline.

The system therefore had to move to an asynchronous model.

The new workflow became:

QR Scan to PENDING to RabbitMQ to Printer to Webhook then to CHECKED_IN

The application now publishes a print request to a message queue instead of waiting for an immediate printer response.

The printer consumes the message and, after the simulated print completes, sends a callback to the FastAPI webhook.

The attendee is only changed to CHECKED_IN after the webhook confirmation is received.

## Scope Delta

### Dropped

The following approach was dropped from the active implementation:

- Direct synchronous waiting for the printer to return a successful response.
- Immediate transition from QR scan to CHECKED_IN.
- The previous polling-based implementation was also deprecated and moved into the `legacy_polling` directory as historical implementation evidence.

### Modified

The following behaviour was modified:

- The attendee status now changes to PENDING before printing is completed.
- Badge-print requests are sent through RabbitMQ instead of being handled through a direct synchronous call.
- The printer now operates as a separate consumer process.
- The FastAPI webhook receives confirmation after the simulated print operation.
- CHECKED_IN is only recorded after successful webhook confirmation.

### Added

The pivot introduced:

- RabbitMQ as the message broker.
- Pika for Python communication with RabbitMQ.
- `checkin.py` for initiating the asynchronous print request.
- `printer.py` as the message consumer.
- `webhook.py` as the callback endpoint.
- `rabbit_test.py` for testing RabbitMQ message delivery.
- `PENDING` as an intermediate attendee status.

### Reprioritized

The main priority changed from obtaining an immediate printer response to ensuring reliable communication between independent components.

The implementation priorities became:

1. Accept the attendee scan.
2. Prevent duplicate check-ins.
3. Set the attendee to PENDING.
4. Publish the print request to RabbitMQ.
5. Allow the printer to consume the request.
6. Receive the completion callback through the webhook.
7. Mark the attendee CHECKED_IN only after confirmation.
8. Verify the complete flow after the refactor.

## Architectural Trade-offs

The asynchronous approach introduced additional components and therefore increased the complexity of the system.

The original synchronous approach was simpler because the application directly called the printer and waited for a response.

The new approach requires RabbitMQ, a printer consumer, a webhook endpoint and persistent attendee state.

However, the asynchronous approach better matches the client's new requirement because the kiosk does not have to wait for the printer operation to complete before continuing.

The PENDING state also makes the status of an unfinished print job explicit rather than incorrectly showing CHECKED_IN before printing has completed.

## Regression Check

After the refactor, I tested the new workflow end to end.

For the temporary test attendee QR-004:

NOT_CHECKED_IN to PENDING to RabbitMQ to Printer to Webhook then finally to CHECKED_IN

The printer successfully received the RabbitMQ message.

The printer successfully called the FastAPI webhook.

The webhook returned HTTP 200.

The attendee status was then updated to CHECKED_IN in `attendees.json`.

I also scanned an attendee who was already checked in and confirmed that the system returned:

"Attendee has already checked in"

This confirmed that duplicate check-in protection continued to work after the architectural change.

## Evidence of Deprecated Code

The original Day 3 polling implementation was not permanently destroyed.

The following files were moved into `legacy_polling`:

- `warehouse.py`
- `poller.py`
- `cache.py`
- `stock_api.py`

These files are no longer part of the active implementation.

Moving them into `legacy_polling` makes the deprecated architecture visible while preventing it from being treated as the current solution.

## What the Pivot Cost

The pivot required learning and integrating several new concepts.

The main additional work included:

- Installing and configuring RabbitMQ and Erlang.
- Learning how RabbitMQ queues work.
- Learning the producer and consumer model.
- Connecting Python to RabbitMQ using Pika.
- Creating a webhook callback using FastAPI.
- Managing attendee state across separate Python processes.
- Introducing persistent state through `attendees.json`.
- Testing communication across multiple running processes.
- Debugging connection, authentication and server-startup issues.

The pivot therefore required more than changing a single endpoint. It required restructuring how the components communicate.

## Final Result

The final implementation follows the asynchronous client requirement:

QR Scan to PENDING to RabbitMQ to Printer to Webhook then finally to CHECKED_IN

The system was tested with multiple attendees and duplicate-scan protection.

The original implementation was preserved as deprecated code in `legacy_polling`, while the new asynchronous implementation became the active approach.

The pivot therefore resulted in a genuine architectural change rather than a cosmetic modification.