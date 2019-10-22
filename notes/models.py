from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()        
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title