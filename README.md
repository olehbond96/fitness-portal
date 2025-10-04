# Fitness Portal

Django project for managing trainers, athletes, workouts and training plans.

## Features

* 4 models with relationships: Trainer, Athlete, Workout, WorkoutPlan
* Custom User model (Trainer extends AbstractUser)
* Full CRUD functionality for all models
* Search functionality on all list pages
* Pagination
* Admin panel for data management
* Responsive Bootstrap design

## Installation

**Requirements:**
* Python 3.11 or 3.12 (Python 3.13 has compatibility issues with Django)

**Steps:**
```bash
git clone https://github.com/yourusername/fitness-portal.git
cd fitness-portal
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
