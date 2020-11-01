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

    def add_activity(self, date_time=None, steps=0, duration=0, distance=0, user=None):
        """
        Add an activity for this type of activity.

        Args:
            date_time: A timezone aware python date time for the activity.
            steps: The number of steps in the activity as an int.
            duration: The duration in seconds of the activity.
            distance: The distance traveled in miles as a float.
            user: ForeignKey to the user who did this activity.

        Returns:
            An instance of Activity representing the newly created activity.
        """
        return self.activity_set.create(
            date=date_time, steps=steps, duration=duration, distance=distance, user=user
        )

    def get_activities_by_month(self, month, user=None):
        """
        Get all activities for the specified month.

        Args:
            month: Int representing the month of year (E.G 11 = November).
            user: Only return activites for the specified user.

        Returns:
            A Django query set matching all activities in the specified month.
        """
        if user is None:
            return self.activity_set.filter(date__month=month)
        else:
            return self.activity_set.filter(date__month=month, user=user)


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

    def get_activity_type_name(self):
        """
        Get the name of the associated ActivityType for this activity.

        Returns:
            The string representation of the associated ActivityType.
        """
        return self.activity_type.__str__()
