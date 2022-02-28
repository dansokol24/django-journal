from django.db import models

# Create your models here.
class Entry(models.Model):
    date = models.DateField()
    heading = models.CharField(max_length=70)
    content = models.TextField(null = True, blank = True)
    
    class Meta:
        ordering = ('date', )