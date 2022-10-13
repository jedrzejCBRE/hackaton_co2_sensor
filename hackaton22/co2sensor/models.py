from django.db import models

# Create your models here.
class PPMreading(models.Model):

    reading = models.FloatField(blank=True, null=True)
