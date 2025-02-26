import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here. (users, contacts, tasks)


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, default="default@gmx.de")
    phone_number = PhoneNumberField(blank=True)
    profileColor = models.CharField(max_length=30, default="#1FD7C1")

    class Meta:
        ordering = ['last_name']


# one task to many subtasks
class Subtask(models.Model):
    subtask_name = models.CharField(max_length=30, default="subtask")
    finished = models.BooleanField(default=False)


class Task(models.Model):
    TASK_CATEGORIES = [
        ("feedback", "Feedback"),
        ("todo", "To Do"),
        ("progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("urgent", "Urgent"),
    ]

    TYPE_CHOICES = [
        ("technical_task", "Technical Task"),
        ("user_story", "User Story"),
    ]

    task_name = models.CharField(max_length=30)
    description = models.TextField(default="beschreibung!")
    subtasks = models.ManyToManyField(Subtask, blank=True)
    assigned_to = models.ManyToManyField(Contact, blank=True)
    due_date = models.DateField(default=datetime.date.today)
    category = models.CharField(
        max_length=20, choices=TASK_CATEGORIES, default="todo")
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="medium")
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="user_story")

    class Meta:
        ordering = ['task_name']


class User(models.Model):
    email = models.EmailField(max_length=254, default="default@gmx.de")
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['email']
