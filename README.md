#  Task Manager

A full-stack Task Management web application built with **Flask**, **SQLite**, and vanilla **JavaScript**. It provides a complete RESTful API for managing tasks (Create, Read, Update, Delete) with a clean, responsive frontend that updates in real time without page reloads.

##  Features

- Add new tasks
- Mark tasks as completed / pending
- Delete tasks
- Real-time UI updates using JavaScript `fetch()` (no page reloads)
- RESTful API backend built with Flask
- Persistent storage using SQLite
- Clean, responsive UI

##  Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| Database | SQLite |
| Frontend | HTML5, CSS3, JavaScript (Fetch API) |
| Templating | Jinja2 |


##  Installation & Setup

1. **Clone the repository**

2. **Install dependencies**
   
3. **Run the application**

4. **Open in browser**

The SQLite database (`tasks.db`) and the `tasks` table are created automatically the first time the app runs.


##  API Endpoints

| Method | Endpoint | Description |
| `GET` | `/api/tasks` | Fetch all tasks |
| `POST` | `/api/tasks` | Create a new task |
| `PUT` | `/api/tasks/<id>` | Update a task's status |s
| `DELETE` | `/api/tasks/<id>` | Delete a task |


##  Future Improvements

- User authentication (so each user manages their own tasks)
- Migrate from SQLite to PostgreSQL/MySQL for production use
- Add due dates and priority levels for tasks
- Deploy with a production WSGI server (Gunicorn)

