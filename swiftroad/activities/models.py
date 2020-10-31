from django.db import models
from django.contrib.auth.models import User


class ActivityType(models.Model):
    """An activity type."""

    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    """An activity that a user does on a given day"""

    date = models.DateTimeField("Activity Date and Time")
    steps = models.IntegerField()
    duration = models.IntegerField()
    distance = models.FloatField()
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        return f"{self.activity_type} on {self.date}"
