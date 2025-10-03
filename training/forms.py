from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Trainer, Athlete, Workout, WorkoutPlan


class TrainerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Trainer
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "specialization",
            "years_experience",
            "phone_number",
        )


class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = "__all__"
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "notes": forms.Textarea(attrs={"rows": 3}),
        }