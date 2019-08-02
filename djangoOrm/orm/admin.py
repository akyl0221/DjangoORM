from django.contrib import admin
from .models import Task, TaskStatuses

admin.site.register(Task)
admin.site.register(TaskStatuses)


