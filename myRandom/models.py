from django.db import models

# Create your models here.
class myRandom(models.Model):
    title = models.TextField()
    descrition = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool')