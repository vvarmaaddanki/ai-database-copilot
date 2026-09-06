# AI Database Copilot

A Django REST Framework API for securely managing database connection configurations with token-based authentication and CRUD operations.

## 🚀 Features

- Token-based API authentication
- Create database connections
- Retrieve all database connections
- Retrieve a single database connection
- Update database connection details
- Delete database connections
- Protected API endpoints
- PostgreSQL database support
- Django REST Framework serializers and views
- Input validation and error handling

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Token Authentication
- Git & GitHub

## 📁 Project Structure

```text
ai-database-copilot/
│
├── agent/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md
🔐 Authentication
The API uses token-based authentication.
Login endpoint:
POST /api/auth/login/
Example request:
{
    "username": "your_username",
    "password": "your_password"
}
The response provides an authentication token.
Use the token in protected API requests:
Authorization: Token YOUR_TOKEN
🔗 API Endpoints
Method
Endpoint
Description
POST
/api/auth/login/
Obtain authentication token
GET
/api/database-connections/
List database connections
POST
/api/database-connections/
Create database connection
GET
/api/database-connections/<id>/
Retrieve a connection
PUT
/api/database-connections/<id>/
Update a connection
DELETE
/api/database-connections/<id>/
Delete a connection
🧪 API Testing
The API was tested using cURL requests covering:
Authentication
GET requests
POST requests
PUT requests
DELETE requests
Invalid token handling
Non-existent resource handling

⚙️ Local Setup
Clone the repository:
git clone https://github.com/vvarmaaddanki/ai-database-copilot.git
cd ai-database-copilot
Create a virtual environment:
python -m venv venv
Activate it on Windows:
venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Start the development server:
python manage.py runserver
The API will be available at:
http://127.0.0.1:8000/

👨‍💻 Project Contribution
Developed and implemented the database connection REST API functionality, including authentication, CRUD operations, validation, error handling, testing, and API integration
