from django.contrib import admin

# Register your models here.

from . import models


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title", "created")


class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)


class StateAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Priority, PriorityAdmin)
admin.site.register(models.State, StateAdmin)
