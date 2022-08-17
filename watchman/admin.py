from django.contrib import admin

from .models import Profile, Record


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("profile", "record_type", "recorded_at", "timezone")
