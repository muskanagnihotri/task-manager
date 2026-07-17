"""
Task Manager - Flask REST API Project
--------------------------------------
Ye project ek simple Task Manager hai jisme:
1. Flask framework use hua hai (web framework)
2. SQLite database use hua hai (aasani se MySQL/PostgreSQL me switch ho sakta hai)
3. Full REST API bani hai -> GET, POST, PUT, DELETE
4. Frontend (HTML/CSS/JS) is API ko fetch() se call karta hai

Interview me explain karne ke liye:
- "Maine Flask use karke ek RESTful Task Management API banayi hai jisme
   CRUD operations (Create, Read, Update, Delete) implement kiye hain,
   SQLite database ke saath, aur ek frontend jo AJAX/fetch se
   is API ko consume karta hai."
"""

from flask import Flask, request, jsonify, render_template
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "tasks.db"


# ---------------------------
# DATABASE SETUP
# ---------------------------
def init_db():
    """Database aur table banata hai agar exist nahi karti"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)
    conn.commit()
    conn.close()


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # rows ko dict jaisa access karne ke liye
    return conn


# ---------------------------
# FRONTEND ROUTE
# ---------------------------
@app.route("/")
def index():
    """Home page render karta hai (HTML file)"""
    return render_template("index.html")


# ---------------------------
# REST API ROUTES
# ---------------------------

# 1) GET all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    # rows ko JSON serializable list of dict me convert karna
    result = [dict(row) for row in tasks]
    return jsonify(result), 200


# 2) POST - naya task create karna
@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)", (title, "pending")
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": new_id, "title": title, "status": "pending"}), 201


# 3) PUT - task update karna (status change karna)
@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    new_status = data.get("status", "pending")

    conn = get_db_connection()
    conn.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task updated successfully"}), 200


# 4) DELETE - task delete karna
@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5000)