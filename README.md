# Meridian Webhook Prototype

## Meridian Pivot Simulation

This repository contains my individual work throughout the Meridian Pivot simulation, from Day 1 through Day 5.

## Day 1-2: Independent Learning

During Days 1–2, I independently learnt about webhooks and FastAPI.

I built and tested a small webhook prototype that receives stock update information and returns a response.

This was my first practical experience working with FastAPI, webhooks, Pydantic, POST requests and Uvicorn. Most of these concepts were new to me, so I had to learn through independent research, testing and troubleshooting.

## Day 3: Original Stock System

On Day 3, I built the original polling-based stock system required by the initial specification.

The original implementation consisted of:

* `warehouse.py` - simulated warehouse stock source
* `poller.py` - periodically retrieves stock
* `cache.py` - stores the latest stock information
* `stock_api.py` - exposes a stock query endpoint

The original flow was:

Warehouse to Poller to Cache then finally to Stock API

I tested the system using several sample SKUs, including products with available stock, zero stock and an unknown product.

## Day 4: Pivot and Asynchronous Processing

On Day 4, the requirements changed and I moved from the original polling approach to an event-driven workflow using RabbitMQ and webhooks.

I implemented a badge-printing workflow using:

* `checkin.py`
* `printer.py`
* `webhook.py`
* `rabbit_test.py`
* `attendees.json`

The new workflow became:

Attendee Scan to PENDING to RabbitMQ to Printer to Webhook then finally to CHECKED_IN

RabbitMQ was used as the message broker, while FastAPI was used to receive the webhook notification after the simulated printing process.

The Day 4 implementation required me to work with several unfamiliar concepts, including message queues, producers, consumers, asynchronous processing and communication between separate Python processes.

## Day 5: Refactor and Review

On Day 5, I reviewed the pivoted implementation and prepared the repository for the final submission.

The original polling implementation was no longer part of the active architecture. Rather than permanently deleting that work, I moved the original Day 3 files into the `legacy_polling/` directory.

The archived files are:

 `legacy_polling/warehouse.py`
 `legacy_polling/poller.py`
 `legacy_polling/cache.py`
 `legacy_polling/stock_api.py`

This preserves the original implementation as evidence of the pre-pivot work while keeping it separate from the active implementation.

The active implementation is now the RabbitMQ/webhook-based workflow.

I also performed an end-to-end test after the refactor. A test attendee successfully moved through:

NOT_CHECKED_IN to PENDING to CHECKED_IN

The printer received the RabbitMQ message and the FastAPI webhook returned HTTP 200.

## My Learning Evidence

The complete learning and blocker journal is maintained in:

`learning-blocker-journal.md`

The journal documents my learning process, blockers, investigations, solutions, testing and reflections from Day 1 through Day 5.

## Repository Structure

The repository contains:

* The active Day 4–5 RabbitMQ/webhook implementation
* The archived Day 3 polling implementation under `legacy_polling/`
* The combined Day 1–5 learning and blocker journal
* Supporting test and data files

## Current Status

The pivoted implementation was tested successfully end to end.

The original polling implementation has been archived rather than discarded so that the progression from the original specification to the pivoted solution can be reviewed transparently.
