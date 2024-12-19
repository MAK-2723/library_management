# Library Management System API

This repository contains a simple Flask-based RESTful API for managing a library system. It supports CRUD operations for books and members, implements token-based authentication, and includes pagination for managing large datasets.

## Features
- **CRUD for Books**: Add, update, delete, and retrieve book details.
- **CRUD for Members**: Add, update, delete, and retrieve member details.
- **Token-based Authentication**: Secure endpoints using tokens.
- **Pagination**: Efficiently retrieve large datasets in smaller chunks.

---

## 1. How to Run the Application

### Prerequisites
- Python 3.7+
- Flask library

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Initialize the database:
   Run the following command to ensure the database tables are created:
   ```bash
   python -c "from models import init_db; init_db()"
   ```
4. Start the server:
   ```bash
   python app.py
   ```
5. Access the API at `http://127.0.0.1:5000`.

---

## 2. Design Choices Made

### 2.1 Minimal Dependencies
- The project avoids third-party libraries beyond Flask to keep the design simple and lightweight.
- SQLite is used as the database to ensure portability and ease of use.

### 2.2 Authentication
- A custom token-based authentication mechanism is implemented using Python’s standard libraries.
- Tokens are generated using SHA-256 hashing and are stored in memory for simplicity.

### 2.3 Database Design
- **Books Table**:
  - Stores information about books, including title, author, published date, and number of pages.
- **Members Table**:
  - Stores member details, including name, email, and password.

### 2.4 Pagination
- Pagination is implemented for the `/books` endpoint to improve performance when retrieving large datasets.
- Default page size is 5 records per request.

### 2.5 Middleware for Authentication
- Authentication middleware ensures all endpoints (except login) require a valid token.

---

## 3. Assumptions and Limitations

### Assumptions
1. User passwords are stored in plain text (only for demonstration purposes).
   - **Note**: In a production environment, passwords must be hashed and securely stored.
2. Token expiration and storage are not implemented for simplicity.
3. Pagination assumes a fixed page size of 5 records per request.
4. All database queries are executed synchronously, suitable for a simple API.

### Limitations
1. **Security**: The current authentication mechanism is basic and insecure for production use.
   - Use secure token storage (e.g., Redis) and implement token expiration.
   - Encrypt passwords using libraries like `bcrypt`.
2. **Scalability**: SQLite is used as the database, which may not scale well for larger applications.
   - For a production system, consider using PostgreSQL or MySQL.
3. **Error Handling**: Limited error handling is implemented.
   - Extend error handling to cover database constraints, invalid input, etc.
4. **Concurrency**: The in-memory token storage may lead to issues in a multi-threaded environment.
   - Use a database or caching solution for token management in production.

---
