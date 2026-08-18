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