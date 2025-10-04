from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Trainer, Athlete, WorkoutPlan, Workout
from .forms import AthleteForm, WorkoutPlanForm, WorkoutForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
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


class TrainerListView(LoginRequiredMixin, generic.ListView):
    model = Trainer
    paginate_by = 5

    def get_queryset(self):
        queryset = Trainer.objects.all()
        username = self.request.GET.get("username")
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class AthleteListView(LoginRequiredMixin, generic.ListView):
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


class TrainerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Trainer


class AthleteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Athlete


class WorkoutDetailView(LoginRequiredMixin, generic.DetailView):
    model = Workout


class WorkoutPlanDetailView(LoginRequiredMixin, generic.DetailView):
    model = WorkoutPlan

class WorkoutListView(LoginRequiredMixin, generic.ListView):
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


class WorkoutPlanListView(LoginRequiredMixin, generic.ListView):
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


class AthleteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Athlete
    form_class = AthleteForm
    success_url = reverse_lazy("training:athlete-list")


class WorkoutPlanCreateView(LoginRequiredMixin, generic.CreateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutCreateView(LoginRequiredMixin, generic.CreateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("training:workout-list")


class AthleteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Athlete
    form_class = AthleteForm
    success_url = reverse_lazy("training:athlete-list")


class AthleteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Athlete
    success_url = reverse_lazy("training:athlete-list")


class WorkoutPlanUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = WorkoutPlan
    form_class = WorkoutPlanForm
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutPlanDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = WorkoutPlan
    success_url = reverse_lazy("training:workout-plan-list")


class WorkoutUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Workout
    form_class = WorkoutForm
    success_url = reverse_lazy("training:workout-list")


class WorkoutDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Workout
    success_url = reverse_lazy("training:workout-list")

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("training:index")
    else:
        form = AuthenticationForm()
    return render(request, "training/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("training:index")
