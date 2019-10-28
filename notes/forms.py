from django import forms
from .models import Note

# from django.forms import ModelForm


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'body')


class SearchForm(forms.Form):
    search_text = forms.CharField(label='Search', max_length=150)


class SortForm(forms.Form):
    by_title = forms.BooleanField(label="Sort by Title", required=False)
    CHOICES = [('Neither', 'Neither'), ('Descending', 'Descending'), ('Ascending', 'Ascending')]
    asc_or_desc = forms.ChoiceField(choices=CHOICES)