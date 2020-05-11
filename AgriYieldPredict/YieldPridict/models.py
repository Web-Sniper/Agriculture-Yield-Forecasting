from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.BigIntegerField()
    feedback = models.CharField(max_length=250)
    def __str__(self):
        return self.name
class Crops(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    duration = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    def __str__(self):
        return self.name