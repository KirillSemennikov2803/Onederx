from django.contrib import admin

from alarm_service.models import Alarm


@admin.register(Alarm)
class AdminRegistered(admin.ModelAdmin):
    list_display = ("description", "alarm_time_at")
