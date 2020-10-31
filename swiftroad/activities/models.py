from django.db import models
from django.contrib.auth.models import User


class ActivityType(models.Model):
    """
    An activity type (for instance 'Run').
    """

    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    Physical activity that a person logs at a specific time.
    """

    date = models.DateTimeField("Activity Date and Time")
    steps = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    distance = models.FloatField(default=0)
    activity_type = models.ForeignKey(ActivityType, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "activities"

    def __str__(self):
        return f"{self.activity_type} on {self.date}"
