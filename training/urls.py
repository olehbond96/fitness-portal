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
        "athletes/<int:pk>/",
        views.AthleteDetailView.as_view(),
        name="athlete-detail"
    ),
    path("workouts/", views.WorkoutListView.as_view(), name="workout-list"),
    path(
        "workouts/<int:pk>/",
        views.WorkoutDetailView.as_view(),
        name="workout-detail"
    ),
    path(
        "workout-plans/",
        views.WorkoutPlanListView.as_view(),
        name="workout-plan-list"
    ),
    path(
        "workout-plans/<int:pk>/",
        views.WorkoutPlanDetailView.as_view(),
        name="workout-plan-detail"
    ),
]

app_name = "training"
