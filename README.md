# Parts Unlimited API

## Description
This project is a take-home assignment for the Backend Engineer position. It involves creating a RESTful API to manage parts for Parts Unlimited. The API supports CRUD operations on parts and includes an additional endpoint to retrieve the 5 most common words in part descriptions, excluding common and irrelevant words for the Sales team (stop words) like "for", "the", "and", etc.

## Features
- CRUD operations for parts.
- Edpoint to retrieve the 5 most common words in part descriptions.

## Requirements
- Python 3.x
- Django
- Django Rest Framework
- MySQL
- drf-yasg (for API documentation)

## Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/alejomendez1019/Parts-Unlimited-API---Take-Home.git
cd parts_unlimited_api
```

### Step 2: Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure the Database
1. Install MySQL.
2. Create a database
    ```bash
    CREATE DATABASE parts_unlimited;
    ```
    
### Step 5: Configure the Environment Variables
1. Copy the `.env.example` to `.env`.
2. Fill in your database credentials in the `.env` file. You can use the same `SECRET_KEY` provided in the `.env.example` file:
    ```bash
    DB_NAME=parts_unlimited
    DB_USER=your_username
    DB_PASSWORD=your_password
    DB_HOST=your_host
    DB_PORT=your_port
    SECRET_KEY=your_secret_key
    ```

### Step 6: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Load Example Data
```bash
python manage.py loaddata apps/parts/fixtures/initial_data.json
```

### Step 8: Run the Server
```bash
python manage.py runserver
```

## Usage

### Endpoints
**CRUD Operations for Parts**
- **List all parts:**
    ```bash
    GET /api/parts/
    ```
- **Create a new part:**
    ```bash
    POST /api/parts/
    ```
- **Retrieve a part by ID:**
    ```bash
    GET /api/parts/{id}/
    ```
- **Update a part by ID:**
    ```bash
    PUT /api/parts/{id}/
    ```
- **Delete a part by ID:**
    ```bash
    DELETE /api/parts/{id}/
    ```

**Common Words Endpoint**
- **Retrieve the 5 most common words in part descriptions, excluding common and irrelevant words for the Sales team (stop words) like "for", "the", "and", etc.:**
    ```bash
    GET /api/parts/common-words/
    ```
    
## API Documentation
The API documentation is available at the following endpoint:
- [Swagger UI](http://localhost:8000/docs/): Interactive interface to explore and test the API.

## Testing
To run the tests, use the following command:
```bash
python manage.py test
```

## Project Structure
```text
parts_unlimited_api/
├── manage.py
├── apps/
    ├── __init__.py
│   └── parts/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── fixtures/
│       │   └── initial_data.json
│       ├── migrations/
│       ├── models.py
│       ├── serializers.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│       
└── parts_unlimited_api/
    ├── settings/
        ├── __init__.py
        ├── base.py
        ├── local.py
        └── production.py
    ├── __init__.py
    ├── asgi.py
    ├── urls.py
    └── wsgi.py
├── .env.example
├── .gitignore
├── requirements.txt
```

## Security Considerations
In a production environment, it would be recommended to implement security measures such as JWT authentication or API Keys to protect API access. These measures have not been implemented in this take-home project to maintain simplicity and focus on the basic functionalities requested.

**Feel free to reach out if you have any questions or need further clarifications.**