from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "trainers/",
        views.TrainerListView.as_view(),
        name="trainer-list"
    ),
    path(
        "trainers/<int:pk>/",
        views.TrainerDetailView.as_view(),
        name="trainer-detail"
    ),
    path("athletes/", views.AthleteListView.as_view(), name="athlete-list"),
    path(
        "athletes/create/",
        views.AthleteCreateView.as_view(),
        name="athlete-create"
    ),
    path(
        "athletes/<int:pk>/",
        views.AthleteDetailView.as_view(),
        name="athlete-detail"
    ),
    path(
        "athletes/<int:pk>/update/",
        views.AthleteUpdateView.as_view(),
        name="athlete-update"
    ),
    path(
        "athletes/<int:pk>/delete/",
        views.AthleteDeleteView.as_view(),
        name="athlete-delete"
    ),
    path("workouts/", views.WorkoutListView.as_view(), name="workout-list"),
    path(
        "workouts/create/",
        views.WorkoutCreateView.as_view(),
        name="workout-create"
    ),
    path(
        "workouts/<int:pk>/",
        views.WorkoutDetailView.as_view(),
        name="workout-detail"
    ),
    path(
        "workouts/<int:pk>/update/",
        views.WorkoutUpdateView.as_view(),
        name="workout-update"
    ),
    path(
        "workouts/<int:pk>/delete/",
        views.WorkoutDeleteView.as_view(),
        name="workout-delete"
    ),
    path(
        "workout-plans/",
        views.WorkoutPlanListView.as_view(),
        name="workout-plan-list"
    ),
    path(
        "workout-plans/create/",
        views.WorkoutPlanCreateView.as_view(),
        name="workout-plan-create"
    ),
    path(
        "workout-plans/<int:pk>/",
        views.WorkoutPlanDetailView.as_view(),
        name="workout-plan-detail"
    ),
    path(
        "workout-plans/<int:pk>/update/",
        views.WorkoutPlanUpdateView.as_view(),
        name="workout-plan-update"
    ),
    path(
        "workout-plans/<int:pk>/delete/",
        views.WorkoutPlanDeleteView.as_view(),
        name="workout-plan-delete"
),
]

app_name = "training"