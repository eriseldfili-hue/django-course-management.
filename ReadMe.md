Course Management API

This is a course management api project build with Django, DRF, Pandas that allows administrator to manage
courses, teachers and students efficiently. The system supports creating and organizing courses, assigning teachers,
enrolling students and importing data from CSV/Excel files with validation. Here you can see features such as
filtering, searching.

To setup the project:

# Django Course Management API

A Django REST API for managing courses, teachers, students and enrollments.

## Features

- Course management
- Student enrollment
- Teacher assignment
- Pagination for API responses

## Tech Stack

- Python
- Django
- Django REST Framework
- SQLite (development)

## Installation

Clone the repository:

git clone https://github.com/username/django-course-management.git

Create virtual environment:

python -m venv venv

Activate it:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

Run server:

python manage.py runserver

## API Endpoints

- `/courses/`
- `/students/`
- `/teachers/`
- `/enrollments/`

## Author

Eriseld Fili
