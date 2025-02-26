from django.contrib import admin
from .models import Task, Subtask, Contact, User

# Register your models here.
admin.site.register(Task)
admin.site.register(Subtask)
admin.site.register(Contact)
admin.site.register(User)
