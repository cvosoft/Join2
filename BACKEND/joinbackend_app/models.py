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


class Task(models.Model):
    task_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['task_name']


class User(models.Model):
    email = models.EmailField(max_length=254, default="default@gmx.de")
    password = models.CharField(max_length=30)

    class Meta:
        ordering = ['email']
