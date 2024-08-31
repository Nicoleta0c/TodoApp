from django.contrib import admin

from todos.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "description", "completed")
    list_display_links = ("id", "description")
    actions = ["mark_as_completed"]

    @admin.action(description="Mark selected tasks as completed")
    def mark_as_completed(self, request, queryset):
        queryset.update(completed=True)
