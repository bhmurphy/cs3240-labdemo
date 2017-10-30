from django.db import models

# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=50)
    mission_statement = models.CharField(max_length=1000)
    incorpDate = models.DateField()
    files = models.FileField(blank=True)

