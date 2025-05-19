# AI Chat Logger API

This is a Django REST Framework API that logs user chat sessions and AI-generated responses. It supports user registration, login, session and message logging, and Swagger API documentation.

---

## Features

- 🧍 User registration and login
- 💬 Chat session creation
- 🧠 Auto-generated AI replies via OpenAI API
- 🔐 Token-based authentication
- 📜 Swagger/OpenAPI documentation (via `drf-spectacular`)

---

## Tech Stack

- Python 3.9+
- Django 4.x
- Django REST Framework
- DRF Spectacular (Swagger docs)
- SQLite (default) — easily replaceable
- OpenAI API integration

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-chat-logger.git
cd ai-chat-logger/backend
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
