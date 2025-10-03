from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Trainer, Athlete, WorkoutPlan, Workout
from .forms import AthleteForm, WorkoutPlanForm, WorkoutForm


def index(request):
    num_trainers = Trainer.objects.all().count()
    num_athletes = Athlete.objects.all().count()
    num_workouts = Workout.objects.all().count()
    num_workout_plans = WorkoutPlan.objects.all().count()

    context = {
        "num_trainers": num_trainers,
        "num_athletes": num_athletes,
        "num_workouts": num_workouts,
        "num_workout_plans": num_workout_plans,
    }

    return render(request, "training/index.html", context)


class TrainerListView(generic.ListView):
    model = Trainer
    paginate_by = 5

    def get_queryset(self):
        queryset = Trainer.objects.all()
        username = self.request.GET.get("username")
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class AthleteListView(generic.ListView):
    model = Athlete
    paginate_by = 10

    def get_queryset(self):
        queryset = Athlete.objects.select_related("trainer")
        name = self.request.GET.get("name")
        if name:
            queryset = queryset.filter(
                first_name__icontains=name
            ) | queryset.filter(
                last_name__icontains=name
            )
        return queryset


class TrainerDetailView(generic.DetailView):
    model = Trainer


class AthleteDetailView(generic.DetailView):
    model = Athlete


class WorkoutDetailView(generic.DetailView):
    model = Workout


class WorkoutPlanDetailView(generic.DetailView):
    model = WorkoutPlan

class WorkoutListView(generic.ListView):
    model = Workout
    paginate_by = 10

    def get_queryset(self):
        queryset = Workout.objects.select_related(
            "athlete",
            "workout_plan"
        )
        athlete = self.request.GET.get("athlete")
        if athlete:
            queryset = queryset.filter(athlete__last_name__icontains=athlete)
        return queryset


class WorkoutPlanListView(generic.ListView):
    model = WorkoutPlan
    paginate_by = 10

    def get_queryset(self):
        queryset = WorkoutPlan.objects.select_related(
            "trainer",
            "athlete"
        )
        title = self.request.GET.get("title")
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class AthleteCreateView(generic.CreateView):
    model = Athlete
    form_class = AthleteForm
    success_url = reverse_lazy("training:athlete-list")


class WorkoutPlanCreateView(generic.CreateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutCreateView(generic.CreateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("training:workout-list")


class AthleteUpdateView(generic.UpdateView):
    model = Athlete
    form_class = AthleteForm
    success_url = reverse_lazy("training:athlete-list")


class AthleteDeleteView(generic.DeleteView):
    model = Athlete
    success_url = reverse_lazy("training:athlete-list")


class WorkoutPlanUpdateView(generic.UpdateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutPlanDeleteView(generic.DeleteView):
    model = WorkoutPlan
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutUpdateView(generic.UpdateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("training:workout-list")


class WorkoutDeleteView(generic.DeleteView):
    model = Workout
    success_url = reverse_lazy("training:workout-list")
