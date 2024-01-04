# models.py
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Pilot(BaseModel):
    name = models.CharField(max_length=255)

class Flight(BaseModel):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()

