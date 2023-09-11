from django.db import models

# Create your models here.

#creating endpoint model

class MyEndPoint(models.Model):
    slack_name = models.CharField(max_length=200)
    track = models.CharField(max_length=200)
    