from django import forms
from .models import Note

# from django.forms import ModelForm


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')