from django.db import models

# Create your models here.

from django.utils import timezone


class Priority(models.Model):  # The Category table name that inherits models.Model
    name = models.CharField(max_length=100)  # Like a varchar

    class Meta:
        verbose_name = ("Priority")
        verbose_name_plural = ("Priorities")

    def __str__(self):
        return self.name  # name to be shown when called


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TodoList(models.Model):  # Todolist able name that inherits models.Model
    title = models.CharField(max_length=250)  # a varchar
    content = models.TextField(blank=True)  # a text field
    created = models.DateField(
        default=timezone.now().strftime("%Y-%m-%d"))  # a date
    priority = models.ForeignKey(Priority, default="Normal")  # a foreignkey
    state = models.ForeignKey(State, default="Pending")

    class Meta:
        ordering = ["-created"]  # ordering by the created field

    def __str__(self):
        return self.title  # name to be shown when called
