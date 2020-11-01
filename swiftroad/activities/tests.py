import datetime

from itertools import repeat

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from .models import Activity, ActivityType

# Create your tests here.
class ActivityModelTests(TestCase):
    def test_activity_creation(self):
        """
        An example test for the Activity model
        """
        now = timezone.now()
        new_activity = Activity(date=now)
        self.assertIs(new_activity.date, now)

    def test_activity_get_activity_type_name(self):
        """
        Test Activities.models.Activity.get_activity_type_name()
        """
        activity_user = User.objects.create_user(username="testuser", password="12345")
        activity_time = timezone.now()
        activity_name = "Test"
        test_activity = ActivityType(name=activity_name)
        test_activity.save()
        new_activity = test_activity.add_activity(
            date_time=activity_time,
            steps=5000,
            duration=30,
            distance=3.2,
            user=activity_user,
        )
        self.assertEqual(new_activity.get_activity_type_name(), "Test")


class ActivityTypeModelTests(TestCase):
    def test_activity_type_creation(self):
        """
        An example test for the ActivityType model
        """
        activity_name = "Test"
        new_activity = ActivityType(name=activity_name)
        self.assertIs(new_activity.name, activity_name)

    def test_activity_type_add_activity(self):
        """
        Test Activities.models.ActivityType.add_activity()
        """
        activity_user = User.objects.create_user(username="testuser", password="12345")
        activity_time = timezone.now()
        activity_name = "Test"
        test_activity = ActivityType(name=activity_name)
        test_activity.save()
        test_activity.add_activity(
            date_time=activity_time,
            steps=5000,
            duration=30,
            distance=3.2,
            user=activity_user,
        )
        self.assertEqual(test_activity.activity_set.count(), 1)

    def test_activity_type_get_activities_by_month(self):
        """
        Test Activities.models.ActivityType.get_activities_by_month()
        """
        minute = timezone.timedelta(minutes=1)
        now = timezone.now()
        activity_user_one = User.objects.create_user(
            username="testone", password="12345"
        )
        activity_user_two = User.objects.create_user(
            username="testtwo", password="12345"
        )
        test_activity = ActivityType(name="Test")
        test_activity.save()
        for minute_offset in range(5, 0, -1):
            activity_time = now - (minute * minute_offset)
            test_activity.add_activity(
                date_time=activity_time,
                steps=100,
                duration=60,
                distance=0.1,
                user=activity_user_one,
            )
            test_activity.add_activity(
                date_time=activity_time,
                steps=100,
                duration=60,
                distance=0.1,
                user=activity_user_two,
            )

        self.assertEqual(
            test_activity.get_activities_by_month(
                timezone.now().month, user=activity_user_one
            ).count(),
            5,
        )
        self.assertEqual(
            test_activity.get_activities_by_month(
                timezone.now().month, user=activity_user_one
            ).count(),
            5,
        )
        self.assertEqual(
            test_activity.get_activities_by_month(timezone.now().month).count(), 10
        )
