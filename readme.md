# Library Management System API

This project is a Flask-based **Library Management System API** that allows CRUD operations for managing books and members. The API also supports search functionality, pagination, and token-based authentication.

---

## (a) How to Run the Project

### Prerequisites
1. **Python**: Make sure Python 3.7 or later is installed on your system.
2. **pip**: Ensure the Python package manager is installed.

### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone <repository-link>
   cd library-management-system
   ```

2. **Install Dependencies**:
   Create a virtual environment and install required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   Start the server by running:
   ```bash
   python app.py
   ```
   
4. **Access the API**:
   The API will be accessible at:
   ```plaintext
   http://127.0.0.1:5000
   ```

### Testing the API
- Use **Postman**, **Thunder Client** (VS Code), or **cURL** to interact with the API.
- Example cURL command:
  ```bash
  curl -X GET http://127.0.0.1:5000/books -H "Authorization: Bearer securetoken"
  ```

---

## (b) Design Choices Made

### 1. **Framework: Flask**
Flask was chosen for its lightweight and modular nature, allowing the application to be easily extended.

### 2. **Endpoints**
- CRUD operations are supported for both books and members, ensuring comprehensive data management.
- Search functionality is implemented using query parameters for books (e.g., `q` for title/author).
- Pagination is supported for efficient data retrieval, especially for large datasets.

### 3. **Token-Based Authentication**
- Authentication ensures that only authorized users can interact with the API.
- A static token (`securetoken`) is used for simplicity in this implementation.

### 4. **Data Storage**
- Data is stored in-memory using Python dictionaries for this implementation, making it lightweight and fast.
- While this approach is suitable for demonstration purposes, a production system would use a relational database like SQLite or PostgreSQL.

### 5. **Error Handling**
- The API includes structured error messages for invalid requests (e.g., missing token, invalid book ID).
- Status codes are returned based on the HTTP method (e.g., `200 OK`, `404 Not Found`, `405 Method Not Allowed`).

---

## (c) Assumptions and Limitations

### Assumptions
1. **Books and Members**:
   - Book IDs and member IDs are integers and unique.
   - Titles and authors are strings, and a book must have both fields.

2. **Authentication**:
   - A single static token (`securetoken`) is used for simplicity.
   - The token must be included in the `Authorization` header.

3. **Pagination**:
   - Default pagination parameters: `page=1` and `per_page=5`.
   - If no pagination is provided, the first 5 results are returned.

### Limitations
1. **Data Persistence**:
   - Data is not persisted across application restarts as it is stored in-memory.
   - A database (e.g., SQLite) would be required for a production-ready system.

2. **Authentication**:
   - The static token approach is not secure for production. In real-world applications, JWT or OAuth2 should be used.

3. **Scalability**:
   - The current implementation is suitable for small-scale applications.
   - For large-scale applications, optimization and database integration would be necessary.

4. **Error Messages**:
   - Error responses are functional but could be expanded to include more details.

---

## Example Endpoints

### 1. Fetch All Books
- **Endpoint**: `/books`
- **Method**: `GET`
- **Description**: Retrieves all books with optional pagination.
- **Query Parameters**:
  - `page` (optional): Page number (default is 1).
  - `per_page` (optional): Number of results per page (default is 5).
- **Example**:
  ```bash
  curl -X GET http://127.0.0.1:5000/books?page=1&per_page=3 -H "Authorization: Bearer securetoken"
  ```

### 2. Add a Book
- **Endpoint**: `/books`
- **Method**: `POST`
- **Description**: Adds a new book.
- **Request Body**:
  ```json
  {
    "title": "1984",
    "author": "George Orwell"
  }
  ```
- **Example**:
  ```bash
  curl -X POST http://127.0.0.1:5000/books \
  -H "Authorization: Bearer securetoken" \
  -H "Content-Type: application/json" \
  -d '{"title": "1984", "author": "George Orwell"}'
  ```

### 3. Search Books
- **Endpoint**: `/books`
- **Method**: `GET`
- **Description**: Searches for books by title or author.
- **Query Parameter**: `q` (title or author keyword).
- **Example**:
  ```bash
  curl -X GET http://127.0.0.1:5000/books?q=Orwell -H "Authorization: Bearer securetoken"
  ```

### 4. Update a Book
- **Endpoint**: `/books/<book_id>`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "title": "Animal Farm",
    "author": "George Orwell"
  }
  ```
- **Example**:
  ```bash
  curl -X PUT http://127.0.0.1:5000/books/1 \
  -H "Authorization: Bearer securetoken" \
  -H "Content-Type: application/json" \
  -d '{"title": "Animal Farm", "author": "George Orwell"}'
  ```

### 5. Delete a Book
- **Endpoint**: `/books/<book_id>`
- **Method**: `DELETE`
- **Example**:
  ```bash
  curl -X DELETE http://127.0.0.1:5000/books/1 -H "Authorization: Bearer securetoken"
  ```

