import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here. (users, contacts, tasks)


class Contact(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, default="default@gmx.de")
    phoneNumber = PhoneNumberField(blank=True)
    profileColor = models.CharField(max_length=30, default="#1FD7C1")

    class Meta:
        ordering = ['firstName']

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Task(models.Model):
    TASK_CATEGORIES = [
        ("feedback", "Feedback"),
        ("todo", "To Do"),
        ("progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("Urgent", "Urgent"),
    ]

    TYPE_CHOICES = [
        ("Technical Task", "Technical Task"),
        ("User Story", "User Story"),
    ]

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    # subtasks = models.ManyToManyField(Subtask, blank=True)
    assigned_to = models.ManyToManyField(Contact, blank=True)
    due_date = models.DateField(default=datetime.date.today)
    category = models.CharField(
        max_length=20, choices=TASK_CATEGORIES, default="todo")
    priority = models.CharField(
        max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    type = models.CharField(
        max_length=20, choices=TYPE_CHOICES, default="User Story")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title}"


class Subtask(models.Model):
    subtask_name = models.CharField(max_length=30, default="subtask")
    finished = models.BooleanField(default=False)
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="subtasks", null=True)

    def __str__(self):
        return f"{self.subtask_name}"


class User(models.Model):
    email = models.EmailField(max_length=254, default="default@gmx.de")
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['email']
