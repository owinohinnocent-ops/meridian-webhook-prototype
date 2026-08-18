# Learning & Blocker Journal

## Day 1 - Independent Learning

**Date:** 18 August 2026

### Unfamiliar Tool/Concept
Webhook verification

### Starting Knowledge
I am new to webhook verification. I understand that webhooks allow one system to send information/data to another system when an event occurs, but I do not yet understand how webhook requests are verified or how to implement webhook verification.

### Learning Objective
I want to understand how webhook verification works and build a small working prototype independently.

### Independent Learning Rule
During Days 1-2, I will research and experiment independently without receiving technical how-to assistance from teammates or instructors.

### Initial Questions
1. What is a webhook?
2. How is a webhook different from polling?
3. What is contained in a webhook request?
4. Why does a webhook need verification?
5. What is a webhook signature?
6. How does a server verify a webhook signature?

### Blocker 1 - Incorrect File Extension

**Problem:**  
I initially created the learning journal as `learning-blocker-journal` without the `.md` extension.

**How I identified it:**  
I used the `git status` command and noticed Git listed the file as `learning-blocker-journal`. I then used the `dir` command in the VS Code terminal to inspect the actual filename.

**Resolution:**  
I renamed the file to `learning-blocker-journal.md` using the VS Code Explorer and verified the filename again using `dir`.

**What I learned:**  
File extensions are important because they identify the type of file. The `.md` extension indicates that the file is a Markdown document.

### Blocker 2 — Git Push Could Not Resolve GitHub

**Problem:**  
When I tried to push my Day 1 journal to GitHub using `git push`, Git returned the error: `Could not resolve host: github.com`.

**Investigation:**  
I first confirmed that GitHub was accessible through my web browser. I then tested the connection from the terminal using `ping github.com` and `curl.exe -I https://github.com`. The HTTPS request returned `HTTP/1.1 200 OK`, confirming that my computer could reach GitHub. I also checked the Git remote using `git remote -v` and confirmed that it pointed to the correct repository. I checked both the HTTP and HTTPS Git proxy settings and found that no proxy was configured.

**Resolution:**  
I configured Git to use HTTP/1.1 with `git config --global http.version HTTP/1.1` and retried `git push`. The push succeeded.

**What I learned:**  
I learned that a Git push problem does not necessarily mean that the repository or commit is wrong. I learned how to distinguish between a Git configuration/network problem and a repository problem by testing each part separately.

## Webhook and FastAPI Learning Checkpoint

### What I Learnt

I started building the webhook and learned some basics of FastAPI and Python along the way.

I learned that FastAPI is used to build APIs in Python, while Uvicorn runs the application so I can test it locally.

I also learned that a POST request is used to send information to the server. Our webhook is `/webhook`, which is where the stock information is sent.

I was introduced to Pydantic and `BaseModel`. I understood them as a way of defining what information our webhook should receive. I created a `StockUpdate` model with:

* `product_id` as text
* `quantity` as a whole number

I then tested the webhook using the Swagger page. I sent:

`{
  "product_id": "SKU-1001",
  "quantity": 25
}`


The terminal showed:

`product_id='SKU-1001' quantity=25`

I also got `200 OK`, which showed that the request worked.

### Blocker Encountered

I got an error saying:

`NameError: name 'stock' is not defined`

After checking the code, I realized I had accidentally put `app = FastAPI()` and `@app.post("/webhook")` on the same line. I separated them and saved the file. The server then started successfully.

### My core lesson

I now understand that a webhook can receive information through a POST request. I also understand the basic idea of using a Pydantic model to define the information we expect to receive.

The basic flow I learned today is:

`POST request after which a webhook then Pydantic checks the data and finally Python function receives the data`

This was my first successful test of a webhook receiving stock information.

