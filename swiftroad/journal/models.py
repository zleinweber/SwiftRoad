from django.db import models

# Create your models here.
class User(models.Model):
    """A user of the application"""

    username = models.CharField(max_length=64)


class Activity(models.Model):
    """An activity that a user does on a given day"""

    activity_date = models.DateTimeField("Activity Date and Time")
    activity_type = models.CharField(max_length=64)
    activity_steps = models.IntegerField()
    activity_duration = models.IntegerField()
    activity_distance = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
