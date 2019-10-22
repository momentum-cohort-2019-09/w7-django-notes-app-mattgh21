from django.db import models
from django.utils import timezone
from django.forms import ModelForm


# Create your models here.
class Note(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()        

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.updated_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']