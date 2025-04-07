# Quora-like Q&A Platform

A Django-based question and answer platform inspired by Quora, implementing core functionality for user interactions.

## Features

- **User Authentication**:
  - User registration with username, email, and password
  - Login/logout functionality
  - Protected routes for authenticated users

- **Question Management**:
  - Create new questions
  - View all questions in chronological order
  - View individual question details

- **Answer System**:
  - Post answers to questions
  - View all answers for a question
  - Like/unlike answers

## Technologies Used

- **Backend**:
  - Python 3
  - Django 4.x
  - Django Authentication System

- **Frontend**:
  - HTML5
  - Bootstrap 5
  - Django Templates

- **Database**:
  - SQLite (default Django DB)
 
    
## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sreerangk/Quora-clone.git
   cd quora-clone
   ```
2.Create and activate virtual environment:
    -python -m venv venv
    -source venv/bin/activate
    
3.Install dependencies:
  - pip install -r requirements.txt

4.Run migrations:
   -python manage.py migrate

5.Create superuser (admin):
  - python manage.py createsuperuser

6.Run development server:
  -python manage.py runserver
