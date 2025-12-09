# 📝 To-Do List Web App (with Login/Logout)

A complete **Fullstack To-Do List Application** built using **Flask**, featuring secure user authentication and a task management system.

---

## 🚀 What Are We Building?

A clean and functional To-Do List web application where:

### 🔐 Core User Features
- **User Login** – Log in using username & password  
- **User Logout** – End session safely  
- **User Registration** – Create a new account  
- **Create Task** – Add new To-Do items  
- **View Tasks** – See all tasks for your account  
- **Update Task** – Edit task title (cannot be empty)  
- **Delete Task** – Remove tasks anytime  

---

## 🛠 Technologies & Tools

| Tool/Library | Purpose |
|--------------|---------|
| **Flask** | Main Python web framework |
| **SQLite** | Local lightweight database |
| **SQLAlchemy** | ORM to interact with database |
| **Flask-WTF** | Form handling + validation |
| **Jinja2** | Template engine for dynamic HTML |
| **Flask-Login** | Manage user login sessions |

---

## 📁 Project Folder Structure

```
ToDo_Flask/
│
├── run.py
│
└── app/
    ├── __init__.py
    ├── models.py
    │
    ├── routes/
    │   ├── __init__.py
    │   ├── auth.py      # login, logout, register
    │   └── task.py      # CRUD for tasks
    │
    ├── templates/
    │   ├── base.html
    │   ├── login.html
    │   ├── register.html
    │   └── tasks.html
    │
    └── static/
        ├── css/
        │   └── style.css
        │
        └── js/
            └── main.js
```

---

## 🔧 How It Works (Short Overview)

- The `run.py` file starts the app.
- `app/__init__.py` creates the Flask instance and initializes extensions.
- `models.py` defines the `User` and `Task` database models.
- `routes/auth.py` handles registration, login, and logout.
- `routes/task.py` handles task creation, editing, viewing, and deletion.
- Templates use Jinja2 to dynamically render content.
- Flask-Login keeps users logged in using secure session cookies.

---

## ✔ Next Steps

- Add categories for tasks  
- Add task deadlines  
- Add dark/light theme  
- Deploy the app on PythonAnywhere / Render  

---

## 🎉 Final Notes  
This structure is scalable, beginner-friendly, and follows good Flask practices.  
Perfect for portfolio or real-world usage.