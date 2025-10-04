from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Trainer, Athlete, WorkoutPlan, Workout


@admin.register(Trainer)
class TrainerAdmin(UserAdmin):
    list_display = ["username", "specialization", "years_experience", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        ("Trainer Info", {"fields": ("specialization", "years_experience", "phone_number")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Trainer Info", {"fields": ("specialization", "years_experience", "phone_number")}),
    )


@admin.register(Athlete)
class AthleteAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "trainer", "date_of_birth"]
    list_filter = ["trainer"]
    search_fields = ["first_name", "last_name", "email"]


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ["title", "athlete", "trainer", "start_date", "end_date"]
    list_filter = ["trainer", "start_date"]
    search_fields = ["title", "athlete__first_name", "athlete__last_name"]
    date_hierarchy = "created_at"


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["athlete", "date", "duration_minutes", "completed"]
    list_filter = ["completed", "athlete", "date"]
    search_fields = ["athlete__first_name", "athlete__last_name", "notes"]
    date_hierarchy = "date"