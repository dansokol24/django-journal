from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateTimeField()
    header = models.CharField(max_length=70)
    content = models.TextField()
    
    class Meta:
        ordering = ('date',)