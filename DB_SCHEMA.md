# Database Schema

## Models Overview

The Fitness Portal uses 4 main models with the following relationships:

### 1. Trainer (extends AbstractUser)
- Custom user model for trainers
- **Fields:**
  - username (inherited)
  - email (inherited)
  - password (inherited)
  - first_name (inherited)
  - last_name (inherited)
  - specialization (CharField)
  - years_experience (PositiveIntegerField)
  - phone_number (CharField)

### 2. Athlete
- **Fields:**
  - first_name (CharField)
  - last_name (CharField)
  - email (EmailField, unique)
  - date_of_birth (DateField)
  - trainer (ForeignKey to Trainer, CASCADE)

### 3. WorkoutPlan
- **Fields:**
  - title (CharField)
  - description (TextField)
  - trainer (ForeignKey to Trainer, CASCADE)
  - athlete (ForeignKey to Athlete, CASCADE)
  - created_at (DateTimeField, auto_now_add)
  - start_date (DateField)
  - end_date (DateField)

### 4. Workout
- **Fields:**
  - athlete (ForeignKey to Athlete, CASCADE)
  - workout_plan (ForeignKey to WorkoutPlan, SET_NULL, nullable)
  - date (DateField)
  - duration_minutes (PositiveIntegerField)
  - notes (TextField, blank)
  - completed (BooleanField)

## Relationships

## Key Design Decisions

1. **Trainer extends AbstractUser** - Allows trainers to login and use Django's built-in authentication
2. **CASCADE delete** - When trainer/athlete is deleted, related records are also deleted
3. **SET_NULL for WorkoutPlan in Workout** - Workouts remain even if plan is deleted
4. **EmailField unique** - Each athlete has unique email address