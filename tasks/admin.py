from django.contrib import admin
from django.contrib.admin.sites import site
from tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    pass


site.register(Task, TaskAdmin)
