from django.contrib import admin
from .models import Note  # Import Note instead of Student

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')