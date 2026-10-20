from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content'] # We deliberately leave out 'user' so they can't assign notes to others