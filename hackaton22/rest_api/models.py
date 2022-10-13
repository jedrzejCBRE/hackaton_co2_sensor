from django.db import models

# Create your models here.
class MotorSpeed(models.Model):
    hz_speed = models.FloatField(blank=True, null=True)