# Learning and Blocker Journal

## Day 1 - Independent Learning

**Date:** 18 August 2026

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
3. How does the webhook works?

### First Problem Faced - Incorrect File Extension

**Problem:**  
I initially created the learning journal as `learning-blocker-journal` without the `.md` extension.

**How I identified it:**  
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

### Key Learning

Today I understood better how the webhook works after receiving the information. I learned that the function can return a response to the system that sent the request.

I also understood better why we use Pydantic. It checks that the information being sent is in the format we expect. Seeing the error when I entered `"twenty five"` helped me understand this better than just reading about it.

### Most Important Lesson 

I am still learning and I don't understand everything yet, but I can now follow what happens when a stock update is sent to the webhook and how the application responds to it.