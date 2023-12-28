from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class TaskType(models.Model):
    name = models.CharField(max_length=255, null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255, null=False)


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=False)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = "LO", _("Low")
        NORMAL = "NO", _("Normal")
        HIGH = "HI", _("High")
        URGENT = "UR", _("Urgent")

    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    deadline = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=2, choices=Priority.choices, default=Priority.NORMAL)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="tasks")

    def __str__(self):
        return f"{self.name} with {self.priority} priority"
