from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    feedback = models.CharField(max_length=250)

