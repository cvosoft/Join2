from django.db import models

# Create your models here. (users, contacts, tasks)
    #email
    #models.PhoneNumberField(_(""))
    #profile_color

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Task(models.Model):
    task_name = models.CharField(max_length=30)

class User(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)