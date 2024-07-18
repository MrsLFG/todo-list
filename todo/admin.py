from django.contrib import admin
from django.contrib.auth.models import Group

from todo.models import Task, Tag


admin.site.unregister(Group)
admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["content", "done", "deadline", ]
    list_filter = ["deadline", "done", ]
    search_fields = ["content", ]
