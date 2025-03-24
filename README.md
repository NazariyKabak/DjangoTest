# Django Event Management API

This is a Django-based RESTful API for managing events such as conferences, meetups, and more.  
It supports user registration, authentication, event CRUD operations, and event registrations.

---

## Features

- **User Registration & Authentication** (JWT)
- **CRUD for Events** (Create, Read, Update, Delete)
- **Event Registration** (Users can register for events)
- **Event Filtering** (by date, location, and organizer)
- **REST API** with Postman support
- **SQLite** used as the default database
- **Modular code structure**
  
---

## Tech Stack

- Python 3.12
- Django 5.1.7
- Django REST Framework
- Simple JWT (for token authentication)

---

## Installation

```bash
cd DjangoTest
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver