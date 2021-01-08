from django.contrib import admin

from .models import SubTask, Task, Project


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(SubTask)