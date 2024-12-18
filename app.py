
from flask import Flask, request, jsonify
from functools import wraps
import math

app = Flask(__name__)

# Sample data storage for books and members
books = []
members = []

auth_tokens = {"admin": "securetoken"}  # Simple token-based authentication

# Helper functions
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token.split(" ")[1] not in auth_tokens.values():
            return jsonify({"error": "Unauthorized access"}), 401
        return f(*args, **kwargs)
    return decorated_function

def paginate(items, page, per_page):
    total_items = len(items)
    total_pages = math.ceil(total_items / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    return {
        "data": items[start:end],
        "pagination": {
            "current_page": page,
            "per_page": per_page,
            "total_items": total_items,
            "total_pages": total_pages
        }
    }

# Routes for books
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Library Management System API. Use /books or /members endpoints."})

def get_books():
    query = request.args.get("q")
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))

    filtered_books = books
    if query:
        filtered_books = [
            book for book in books
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()
        ]

    return jsonify(paginate(filtered_books, page, per_page))

@app.route("/books", methods=["GET", "POST"])

@token_required
def add_book():
    data = request.get_json()
    if not data.get("title") or not data.get("author"):
        return jsonify({"error": "Title and author are required"}), 400

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "available": data.get("available", True)
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route("/books/<int:book_id>", methods=["PUT"])
@token_required
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404

    book.update({
        "title": data.get("title", book["title"]),
        "author": data.get("author", book["author"]),
        "available": data.get("available", book["available"])
    })
    return jsonify(book)

@app.route("/books/<int:book_id>", methods=["DELETE"])
@token_required
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"})

# Routes for members
@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)

@app.route("/members", methods=["POST"])
@token_required
def add_member():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({"error": "Name is required"}), 400

    new_member = {
        "id": len(members) + 1,
        "name": data["name"],
        "books_issued": []
    }
    members.append(new_member)
    return jsonify(new_member), 201

@app.route("/members/<int:member_id>", methods=["PUT"])
@token_required
def update_member(member_id):
    data = request.get_json()
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        return jsonify({"error": "Member not found"}), 404

    member.update({
        "name": data.get("name", member["name"]),
        "books_issued": data.get("books_issued", member["books_issued"])
    })
    return jsonify(member)

@app.route("/members/<int:member_id>", methods=["DELETE"])
@token_required
def delete_member(member_id):
    global members
    members = [member for member in members if member["id"] != member_id]
    return jsonify({"message": "Member deleted"})

if __name__ == "__main__":
    app.run(debug=True)
