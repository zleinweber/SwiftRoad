import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Activity

# Create your tests here.
class ActivityModelTests(TestCase):

    def test_activity_model_example(self):
        """An example test for the activity model"""
        now = timezone.now()
        new_activity = Activity(activity_date=now)
        self.assertIs(new_activity.activity_date, now)
