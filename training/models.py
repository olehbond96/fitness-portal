from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Trainer(AbstractUser):
    specialization = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=15, blank=True)

    class Meta:
        verbose_name = "Trainer"
        verbose_name_plural = "Trainers"

    def __str__(self):
        return f"{self.username} ({self.specialization})"

    def get_absolute_url(self):
        return reverse("training:trainer-detail", kwargs={"pk": self.pk})


class Athlete(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="athletes")

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Athlete"
        verbose_name_plural = "Athletes"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("training:athlete-detail", kwargs={"pk": self.pk})


class WorkoutPlan(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="workout_plans")
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="workout_plans")
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Workout Plan"
        verbose_name_plural = "Workout Plans"

    def __str__(self):
        return f"{self.title} - {self.athlete}"

    def get_absolute_url(self):
        return reverse("training:workout-plan-detail", kwargs={"pk": self.pk})


class Workout(models.Model):
    athlete = models.ForeignKey(
        Athlete,
        on_delete=models.CASCADE,
        related_name="workouts"
    )
    workout_plan = models.ForeignKey(
        WorkoutPlan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workouts"
    )
    date = models.DateField()
    duration_minutes = models.PositiveIntegerField()
    notes = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"

    def __str__(self):
        return f"{self.athlete} - {self.date}"

    def get_absolute_url(self):
        return reverse("training:workout-detail", kwargs={"pk": self.pk})

