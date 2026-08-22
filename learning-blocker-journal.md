# Meridian Day 1-3 Learning and Blocker Journal

## Day 1 - Independent Learning

Date: 18/08/2026

### Unfamiliar Tool/Concept
Webhook verification

### My starting Knowledge
I am new to webhook verification. I understand that webhooks allow one system to send information/data to another system when an event occurs, but I do not yet understand how webhook requests are verified or how to implement webhook verification.

### Learning Objective
I want to understand how webhook verification works and build a small working prototype independently.

### Independent Learning Rules to follow
During Days 1-2, I will research and experiment independently without receiving technical how-to assistance from teammates or instructors.

### Learning Questions
1. What is a webhook?
2. How is a webhook different from polling?
3. How does the webhook work?

### First Problem Faced - Incorrect File Extension
  
I initially created the learning journal as `learning-blocker-journal` without the `.md` extension.

### How I identified the problem:  
I used the `git status` command and noticed Git listed the file as `learning-blocker-journal`. I then used the `dir` command in the VS Code terminal to inspect the actual filename.

### How I resolved the issue  
I renamed the file to `learning-blocker-journal.md` using the VS Code Explorer and verified the filename again using `dir`.

### What I learnt  
File extensions are important because they identify the type of file. The `.md` extension indicates that the file is a Markdown document.

### Second Problem Faced - Git Push Could Not Resolve GitHub
  
When I tried to push my Day 1 journal to GitHub using `git push`, Git returned the error: `Could not resolve host: github.com`.

### How I did my investigation 

I first confirmed that GitHub was accessible through my web browser. I then tested the connection from the terminal using `ping github.com` and `curl.exe -I https://github.com`. The HTTPS request returned `HTTP/1.1 200 OK`, confirming that my computer could reach GitHub. I also checked the Git remote using `git remote -v` and confirmed that it pointed to the correct repository. I checked both the HTTP and HTTPS Git proxy settings and found that no proxy was configured.

### How I solved the issue

I configured Git to use HTTP/1.1 with `git config --global http.version HTTP/1.1` and retried `git push`. The push succeeded.

### What I learnt
 
I learnt that a Git push problem does not necessarily mean that the repository or commit is wrong. I learned how to distinguish between a Git configuration/network problem and a repository problem by testing each part separately.

## Webhook and FastAPI Learning

### What I Learnt

I started working on the webhook. Honestly, I realized that I only had basics in Python and FastAPI, so I had to take things slowly and understand what each part of the code was doing.

I learnt that FastAPI is used to build APIs using Python. I also learnt that Uvicorn is used to run the FastAPI application on my computer so that I can test it.

I learnt that a POST request is used to send information to the server. In this case, /webhook is the endpoint that receives the stock update.

I also came across Pydantic and BaseModel. At first I did not understand what they were for. After working through it, I understood that we can use them to define the information we expect to receive. I created a StockUpdate model with product_id and quantity.

I also learnt what an SKU is. I had seen SKU while learning independently but did not know what SKU meant. I now understand that it is used to identify a product.

I tested the webhook using the Swagger page. I sent:

{
  "product_id": "SKU-1001",
  "quantity": 25
}

The terminal showed: product_id='SKU-1001' quantity=25

I also got a 200 OK response. This showed me that the webhook had received the information successfully.

### Problem I Encountered in the Process

I made a few mistakes while setting up the webhook.

One error I got was:

NameError: name 'stock' is not defined

I had to go back and check my code to understand what I had done wrong. I also accidentally put app = FastAPI() and @app.post("/webhook") on the same line. After separating them and saving the file, the application started successfully.

I also initially did not understand where to type some of the commands. For example, I tried running Uvicorn before it was installed. I later installed FastAPI and Uvicorn using pip and continued with the project.

### Most important lesson

The biggest thing I learned today is that I need to understand the code before building/creating a product. I am still learning , but I am beginning to understand how the different parts connect.

For now, I understand the webhook flow as:

POST request, /webhook, FastAPI receives the data, Pydantic checks it, Python function receives the data

I successfully tested the webhook with real stock information today. There is still a lot I don't understand yet, but I have a better starting point than I had before I began.

## Day 2 - Making the Webhook Respond

Date: 19/08/2026

### What I Learnt

Today I continued working on the webhook. Yesterday the webhook could receive the stock information and print it in the terminal. Today I learned how to make it send a response back.

I learned that `print()` only shows information in my terminal, while `return` sends a result back from the function.

I changed my function so that instead of only printing the stock update, it also returns a message together with the product ID and quantity.

I also learned how to include the information we received in the response. Instead of only returning "Stock update received", I changed the response so that it also showed the product ID and quantity. This made it clearer what information the webhook had received.

### Problem I Encountered

I wanted to understand what would happen if the wrong type of information was sent to the webhook. I changed the quantity from a number to `"twenty five"` and tested it.

At first, I entered it without quotation marks and got an error. I corrected the format and tested it again.

This time I got an error saying that the input should be a valid integer. This helped me understand why I wrote `quantity: int` in the `StockUpdate` model. The webhook expects the quantity to be a whole number, so Pydantic rejected the text.

After that, I changed the quantity back to `25` and the webhook worked again.

### My Crucial Learning point

Today I understood better how the webhook works after receiving the information. I learned that the function can return a response to the system that sent the request.

I also understood better why we use Pydantic. It checks that the information being sent is in the format we expect. Seeing the error when I entered `"twenty five"` helped me understand this better than just reading about it.

### Most Important Lesson

I am still learning and I don't understand everything yet, but I can now follow what happens when a stock update is sent to the webhook and how the application responds to it.

## Day 3 - Building the Original Stock System

Date: 20/08/2026

### What I Was Asked to Build

Today, building the original version of the stock system was the task of the day. The requirement was to create a simple system that could get stock information from a warehouse, check for stock updates regularly, store the latest stock information, and allow someone to ask for the stock of a particular product.

I was working on this alone, so I had to figure out each part as I went along. I decided to start with five sample products so that I could test the system with different stock situations.

The five products I used were:

- SKU-1001 - 25 units
- SKU-1002 - 10 units
- SKU-1003 - 0 units
- SKU-1004 - 15 units
- SKU-1005 - 7 units

### What I Built

I started by creating `warehouse.py` to act as the warehouse stock source. It contains the five sample products and their current quantities.

I then created `poller.py`. Its job is to regularly get the latest stock from the warehouse. During testing, I set it to run every 10 seconds instead of waiting five minutes each time. This made it easier to see whether the polling was actually working.

Next, I created `cache.py`. I used it to store the latest stock information in a file called `stock_cache.json`. This meant that the stock information could be saved and later read by another part of the system.

Finally, I created `stock_api.py` using FastAPI. This provided an endpoint where I could enter a product ID and get its current stock quantity.

By the end, the basic flow was: Warehouse to Poller to Cache to Stock API and finally to Product stock response.

### Problems I Encountered

I made several mistakes today while building the system. Most of them were small coding mistakes, but they helped me understand what each part of the system was actually doing.

#### Blocker 1 - The Syntax Error in warehouse.py

When I first tried to run the warehouse code, I got a syntax error because I had forgotten the colon after the `get_stock()` function definition.

The error was:

`SyntaxError: expected ':'`

I went back to the function definition, added the missing colon, saved the file and ran the command again. After fixing it, the warehouse returned the five products and their stock quantities correctly.

#### Blocker 2 - Problems I faced with the Cache

The cache was more difficult for me because I initially wrote the functions incorrectly. I had problems with the `get_cached_stock()` function and also had an import error because `poller.py` was trying to import `update_cache` when that function was not correctly defined in `cache.py`.

I went back through the code and corrected the cache functions.

I also initially used `f` when opening the file but then wrote `file` inside `json.dump()`. This caused:

`NameError: name 'file' is not defined`

I learned that the variable name used when opening the file has to match the variable used when reading or writing to it.

#### Blocker 3 - Poller Was Not Updating the Cache

At one point, `poller.py` was getting the stock and printing it, but I had forgotten to actually call `update_cache(stock)`.

The stock was appearing in the terminal, but it was not being saved to the cache. I added the `update_cache(stock)` line to the polling loop.

After that, `stock_cache.json` was created successfully and contained the five stock records.

#### Blocker 4 - FastAPI Import Error

When I first tried to start the stock API, I got:

`ModuleNotFoundError: No module named 'fastAPI'`

I checked the import and realized that I had written `fastAPI` instead of `fastapi`. After correcting the spelling, the application started successfully.

#### Blocker 5 - API Indentation Problem

The stock API initially did not return the product information correctly. I had accidentally placed the successful `return` statement inside the `if` block that checks whether a product exists.

I corrected the indentation so that the "Product not found" response is only returned when the product does not exist, while the normal stock response is returned when the product is found.

#### Blocker 6 - Server Connection Problem

At one point, I tried opening the API in the browser and got `ERR_CONNECTION_REFUSED`.

I realized that the FastAPI server was no longer running. I started it again using Uvicorn and was then able to access the Swagger page and test the endpoint.

### Testing the Stock API

After fixing the problems, I tested the API using the Swagger page provided by FastAPI.

I tested several different situations.

First, I tested `SKU-1001`. The API returned 25 units, which matched the stock in the warehouse data.

I then tested `SKU-1002`, and the API returned 10 units.

I also tested `SKU-1003`, which had zero stock. The API correctly returned 0 instead of treating the product as missing.

Finally, I tested `SKU-9999`, which was not in my warehouse data. The API returned "Product not found".

The tests gave me the following results:

- SKU-1001 , 25 units - Passed
- SKU-1002 , 10 units - Passed
- SKU-1003 , 0 units - Passed
- SKU-9999 , Product not found - Passed

I was excited and this gave me confidence that the API was reading the cached stock correctly and could handle both existing and unknown products.

### What I Learnt

Day 3 helped me understand how the different parts of the system connect. Before starting, I understood each idea separately, but I was not yet confident about how they would work together.

I now understand that the warehouse provides the stock information, the poller regularly gets the information, the cache stores the latest information, and the API allows another system or user to request the stock for a particular product.

I also learned that debugging is part of building software. I made several mistakes today, but checking the error messages and going back to the code helped me understand what was wrong.

One thing I found particularly useful was seeing the difference between getting the stock and actually storing it. At first my poller was printing the stock, but it was not updating the cache because I had not called `update_cache(stock)`.

I also learned that small things such as spelling, indentation, and variable names can prevent an otherwise correct program from working.

### Day 3 Final Result

By the end of Day 3, I had a working version of the original stock system. I successfully connected the warehouse data, polling process, cache and FastAPI query endpoint.

I committed the Day 3 code to GitHub using commit:

`6b1dd6f - Complete Day 3 Inventory Polling and Stock API`

I also pushed the commit successfully and confirmed that my branch was up to date with `origin/main`.

My final `git status` showed:

`nothing to commit, working tree clean`

This gave me a clean checkpoint before moving to the next stage of the project.

## Day 4 - The Pivot and Asynchronous Processing

Date: 21/08/2026

### What Changed

Today the project changed direction. The original stock system I built on Day 3 used polling, where the system repeatedly checked the warehouse for updates.

The new requirement was to move away from that approach and use an event-driven workflow. For my implementation, I worked with RabbitMQ, a printer process and a FastAPI webhook.

The change was challenging because RabbitMQ and asynchronous processing were still new to me. I understood the general idea, but I had to learn how the different processes communicate and how a message moves through the system.

## What I Built

I created a badge-printing workflow using:

- `checkin.py`
- `printer.py`
- `webhook.py`
- `rabbit_test.py`
- `attendees.json`

The new flow was:

Attendee Scan to PENDING to RabbitMQ to Printer to Webhook then finally to CHECKED_IN

When an attendee is scanned, their status changes to `PENDING`. A print request is then sent to RabbitMQ. The printer acts as a consumer and receives the request. After the simulated printing is completed, the printer sends a request to the FastAPI webhook. The webhook then changes the attendee status to `CHECKED_IN`.

## Problems I faced

### Blocker 1 - RabbitMQ and Erlang Setup

One of the first difficulties I faced was getting RabbitMQ to work correctly. I initially received an `ERLANG_HOME not set correctly` error.

I also encountered an Erlang cookie/authentication issue. This was confusing because I had already installed RabbitMQ Server and Erlang.

I had to stop and investigate the installation and configuration before continuing.

Eventually RabbitMQ was working, and I was able to verify it using the RabbitMQ command-line tools.

### Blocker 2 - Understanding the Printer Process

When I ran `python printer.py`, the terminal only displayed:

`Printer is waiting for print requests...`

At first I thought the program was stuck. I later understood that this was actually the expected behaviour because the printer was a consumer waiting for a message from RabbitMQ.

When a print request was sent, the printer displayed: `Printer received: Print badge for QR-003`

This helped me understand the producer and consumer concept much better.

### Blocker 3 - Webhook Connection Error

When I first connected the printer to the FastAPI webhook, I received:

`WinError 10061`

The connection to `127.0.0.1:8000` was refused.

I initially thought there was something wrong with the code. I later realized that the FastAPI server was not running.

I started it using: `python -m uvicorn webhook:app --reload`

Once Uvicorn was running, the printer was able to communicate with the webhook and I received:
`Webhook response: 200`

### Blocker 4 - Sharing State Between Processes

Another problem was understanding how the attendee status would be updated.

Initially, the attendee information was stored in a Python dictionary inside `checkin.py`. I expected the webhook to be able to update the same dictionary after the badge was printed.

I eventually understood that `checkin.py` and the FastAPI webhook were running as separate Python processes. They therefore did not automatically share the same Python variables.

I changed the implementation to use `attendees.json` as persistent shared state.

This allowed the status to move through:

`NOT_CHECKED_IN to PENDING to CHECKED_IN`

### Testing

I tested the system using the attendee QR codes.

For the final end-to-end test, I added a temporary test attendee with QR code `QR-004`.

The first command returned:

`{'success': True, 'message': 'Badge printing is pending', 'name': 'Test Attendee', 'status': 'PENDING'}`

The printer then received: `Printer received: Print badge for QR-004`

The printer successfully called the webhook and received: `Webhook response: 200`

I then checked `attendees.json` and confirmed that QR-004 had changed to: `CHECKED_IN`

This confirmed that the complete asynchronous workflow was working.

I removed the temporary QR-004 test data afterwards so that the final project data remained clean.

## What I Learnt

The biggest lesson from Day 4 was that changing an architecture is more difficult than simply changing a few lines of code.

I learnt how RabbitMQ can act as a message broker between different processes. I also learnt the difference between a producer and a consumer.

I now understand the basic roles of the components I used:

- RabbitMQ - message broker
- Pika - Python library used to communicate with RabbitMQ
- `checkin.py` - sends the print request
- `printer.py` - consumes the print request
- FastAPI - receives the webhook notification
- Uvicorn - runs the FastAPI application
- Requests - allows the printer to call the webhook
- `attendees.json` - stores the attendee status

I also learned an important debugging lesson. When several components are involved, I should not assume that the whole system is broken. I can test each part separately: the RabbitMQ server, queue, producer, consumer, webhook and persistent state.

## My take on Day 4

Honestly, Day 4 was one of the most challenging parts of the simulation for me because most of the tools and concepts were still new to me.

There were moments when I did not know what was wrong and I had to slow down and investigate one problem at a time. I also made mistakes while working between different PowerShell terminals.

However, I did not stop when I encountered the errors. I kept testing individual components until I could see the complete flow working.

Seeing the printer receive the message, the webhook return `200`, and the attendee finally change to `CHECKED_IN` gave me confidence that I was beginning to understand asynchronous communication rather than just copying code.

## Day 5 - Refactor and Review

Date: 22/08/2026

### What I Did

Today I reviewed the implementation after the pivot and prepared the project for final submission.

According to the instructions provided by PLP, the main Day 5 requirement was to ship the new approach, document what changed, and deal with the parts of the original implementation that no longer fit the new direction.

I reviewed the original polling implementation from Day 3 and identified these files as obsolete for the final architecture:

- `cache.py`
- `poller.py`
- `stock_api.py`
- `warehouse.py`

Instead of permanently destroying the previous work, I moved these files into a `legacy_polling` folder.

This means the old implementation is no longer part of the active implementation, but it is still available as evidence of what I built before the pivot.

## The Scope Change

The original implementation was:

Warehouse to Poller to Cache to Stock API

The pivoted implementation became:

Attendee Scan to PENDING to RabbitMQ to Printer to Webhook to CHECKED_IN

The main change was therefore from a polling-based approach to an event-driven/message-based approach.

The old polling files were no longer needed by the active implementation, so I deprecated them by moving them into `legacy_polling`.

## What Stayed Working

The Day 4 asynchronous workflow continued to work after the Day 5 cleanup.

I verified that RabbitMQ was running and that the FastAPI application could start successfully.

I also ran the printer process and performed another end-to-end test.

For the test attendee QR-004, the system successfully moved through:

`NOT_CHECKED_IN → PENDING → CHECKED_IN`

The printer received the RabbitMQ message and the webhook returned HTTP `200`.

This gave me confidence that the pivoted implementation was still functional after the refactor.

## What I Found Difficult

The hardest part of Day 5 was understanding what should be removed and what should be preserved.

At first, seeing Git report the original polling files as deleted made me concerned that I had lost my Day 3 work.

I checked the project and confirmed that the old files had been preserved inside `legacy_polling`.

This helped me understand the difference between deleting something permanently and deprecating or archiving an old implementation.

I also learned that Git status is useful during a refactor because it shows exactly what has been modified, deleted and added before anything is committed.

## What I Learnt

Day 5 taught me that refactoring is not only about making code shorter or cleaner. It is also about deciding what still belongs to the current requirements and what no longer fits.

I also learnt that previous work can still be valuable even when the requirements change. The Day 3 polling implementation helped me understand the original architecture and gave me a clear basis for understanding what the pivot changed.

Most importantly, I learned that I can remain productive even when I am working with tools that are unfamiliar to me. I still have a lot to learn, but I am becoming more comfortable with investigating problems instead of immediately assuming that I cannot solve them.

## My final take

Looking back at the five days, the biggest change for me was not just the code. It was my approach to learning.

At the beginning, I was very dependent on understanding every technical detail before feeling confident. The simulation forced me to work with unfamiliar concepts, make mistakes, investigate errors and continue moving.

I struggled several times, especially when working with RabbitMQ, asynchronous processing and multiple processes. However, I kept testing and fixing one issue at a time.

The pivot also showed me that software development is not always about finishing the first solution. Requirements can change, and part of engineering is being able to understand the change, identify what no longer fits, preserve useful work, and move forward.

I would not say that I now fully understand all the technologies I used. I am still if not a beginner then intermediate in many of them. However, I am more confident that when I encounter an unfamiliar tool or an error, I can investigate it, learn from it and eventually make progress.

That is probably the most important thing I am taking away from the Meridian Pivot simulation.