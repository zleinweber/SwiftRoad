import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Activity, ActivityType

# Create your tests here.
class ActivityModelTests(TestCase):
    def test_activity_model_example(self):
        """
        An example test for the Activity model
        """
        now = timezone.now()
        new_activity = Activity(date=now)
        self.assertIs(new_activity.date, now)


class ActivityTypeModelTests(TestCase):
    def test_walk_activity_model_example(self):
        """
        An example test for the ActivityType model
        """
        activity_name = "Test Activity"
        new_activity = ActivityType(name=activity_name)
        self.assertIs(new_activity.name, activity_name)
