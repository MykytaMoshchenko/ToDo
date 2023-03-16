from django.contrib import admin
from to_do.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)
    list_filter = ("tags",)


@admin.register(Tag)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)
