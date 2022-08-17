import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from .models import Profile, Record


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    password = factory.Faker("password")


class RecordFactory(DjangoModelFactory):
    class Meta:
        model = Record

    profile = factory.Iterator(Profile.objects.all())
    recorded_at = factory.Faker("date_time_this_month", before_now=True)
    record_type = factory.Iterator([choice[0]
                                   for choice in Record.RecordType.choices])
    timezone = 'UTC'
