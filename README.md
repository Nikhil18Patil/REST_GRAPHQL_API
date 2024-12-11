# Bank Branches API

## Overview
This repository provides an API server to manage and retrieve information about banks and their branches. The solution is implemented in Django and supports both REST APIs and GraphQL queries.

## Features

### REST API Endpoints:
- **Retrieve the list of banks.**
- **Get detailed information about a specific branch using its IFSC code.**

### GraphQL Support:
- **Query bank branches and nested bank details at the `/gql` endpoint.**

### Clean Code:
- Models, serializers, and views are modular and reusable.
- Proper error handling using `try` and `except` blocks.

### Database:
- **PostgreSQL** is used for structured data storage.
- Includes tables for **banks**, **branches**, and a **view** `bank_branches` for efficient querying.

## API Endpoints

### REST APIs

#### GET /api/banks/
Retrieves a list of all banks.

**Response:**
```json
{
    "banks": [
        {"id": 1, "name": "Bank A"},
        {"id": 2, "name": "Bank B"}
    ]
}
```

#### GET /api/branches/<branch_ifsc>/
Retrieves details about a specific branch using its IFSC code.

**Response:**
```json
{
    "branch": {
        "ifsc": "ABC12345678",
        "bank": "Bank A",
        "branch": "Main Branch",
        "address": "123 Street, City",
        "city": "City",
        "district": "District",
        "state": "State"
    }
}
```

### GraphQL

#### Endpoint: /gql/

**Sample Query:**
```graphql
query {
  branches {
    ifsc
    branch
    bank {
      name
    }
    address
    city
    district
    state
  }
}
```

**Sample Response:**
```json
{
  "data": {
    "branches": [
      {
        "ifsc": "ABC12345678",
        "branch": "Main Branch",
        "bank": {"name": "Bank A"},
        "address": "123 Street, City",
        "city": "City",
        "district": "District",
        "state": "State"
      }
    ]
  }
}
```

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL
- Virtual Environment (venv or equivalent)

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-link>
   cd <repository-name>
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   - Configure PostgreSQL and create a database.
   - Create a `.env` file in the root of the project directory and add the following environment variables:
     ```env
     DB_NAME=Banks
     DB_USER=Nikhil
     DB_PASSWORD=Nikhil@18
     DB_HOST=localhost
     DB_PORT=5432
     ```
   - Update `settings.py` to include the environment variables for database configuration.

5. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

### Access the API
- **REST APIs:** [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- **GraphQL:** [http://127.0.0.1:8000/gql/](http://127.0.0.1:8000/gql/)

### Swagger Documentation:
Once the server is running, you can access the Swagger API documentation by navigating to the following URL:

[http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

This allows you to interact with the REST APIs and execute requests directly through the Swagger interface.

## Methodology

### Backend Framework:
- Used Django with Django REST Framework for implementing REST APIs.
- Added GraphQL support using `graphene-django`.

### Database Design:
- **Bank** and **Branch** models were created with a one-to-many relationship.
- A view `bank_branches` combines data for efficient querying.

### Error Handling:
- `try` and `except` blocks ensure robust error handling for both expected and unexpected cases.

### Code Structure:
- **Models:** Defined `Bank` and `Branch` in `models.py`.
- **Serializers:** Handled data transformation and validation in `serializers.py`.
- **Views:** API logic implemented in `views.py`.
