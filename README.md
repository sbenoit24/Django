# AI Chat Logger API

This project is a Django REST Framework-based API that allows users to register, create chat sessions, send messages, and receive AI-generated replies using OpenAI's ChatGPT API. It includes Swagger documentation, token-based authentication, and is fully testable with Postman.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sbenoit24/Django
cd ai-chat-logger/backend

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Add your OpenAI API key

OPENAI_API_KEY=your_openai_api_key_here

5. Apply migrations and create a superuser

python manage.py migrate
python manage.py createsuperuser

6. Run the server

python manage.py runserver

API Endpoints

| Method | Endpoint              | Description                                   |
| ------ | --------------------- | --------------------------------------------- |
| POST   | `/api/register/`      | Register a new user                           |
| POST   | `/api/login/`         | Login and receive auth token                  |
| GET    | `/api/sessions/`      | List user's chat sessions                     |
| POST   | `/api/sessions/`      | Create a new chat session                     |
| GET    | `/api/sessions/<id>/` | Retrieve a specific chat session and messages |
| GET    | `/api/messages/`      | List all messages (admin only)                |
| POST   | `/api/messages/`      | Send a message in a chat session              |
| GET    | `/api/schema/`        | OpenAPI schema (raw JSON)                     |
| GET    | `/api/swagger/`       | Swagger UI (interactive docs)                 |



Testing with Postman
Import the Swagger Schema
Open Postman → Import → Link → paste:

http://127.0.0.1:8000/api/schema/

Register a User

Method: POST

URL: http://127.0.0.1:8000/api/register/

Body (JSON):

{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpassword"
}
Login

Method: POST

URL: http://127.0.0.1:8000/api/login/

Body (JSON):

{
  "username": "testuser",
  "password": "testpassword"
}

Response contains the auth token.

Set the Token in Authorization Header

In Postman, go to Authorization tab

Type: Bearer Token

Token: paste the token from login response

Create a Chat Session

Method: POST

URL: http://127.0.0.1:8000/api/sessions/

Body (JSON):

{
  "title": "My First Chat"
}
Send a User Message

Method: POST

URL: http://127.0.0.1:8000/api/messages/

Body (JSON):

{
  "session": "<session_id>",
  "sender": "USER",
  "message": "Hello AI!"
}
