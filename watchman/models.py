from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Stores the profile data associated with each user, related to 
    :model:`auth.User`
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Creates a :model:`watchman.Profile` object each time a :model:`auth.User` 
    object is created
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Record(models.Model):
    """
    Stores date and time of either entry or exit of an employee from the office,
    related to :model:`watchman.Profile`
    """
    class RecordType(models.TextChoices):
        """
        Stores the type of record, it can be either `I` for `Entry Time` or 
        `O` for `Exit Time`
        """
        IN = 'I', 'Entry Time'
        OUT = 'O', 'Exit Time'
    record_type = models.CharField(
        max_length=1,
        choices=RecordType.choices
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recorded_at = models.DateTimeField()

    class TimezoneType(models.TextChoices):
        """
        Stores the timezone, it can be either `UTC` for `Universal Coordinated
        Time` or `PST` for `Pakistan Standard Time`
        """
        UTC = 'UTC', 'Universal Coordinated Time'
        PST = 'PST', 'Pakistan Standard Time'
    timezone = models.CharField(
        max_length=3,
        choices=TimezoneType.choices,
        default='UTC'
    )

    def __str__(self) -> str:
        return f"{self.profile.user.username} {self.record_type} {self.recorded_at}"
