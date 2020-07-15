import datetime

from django.db import models
from django.dispatch import receiver

from alarm_service.tasks import set_an_alarm


class Alarm(models.Model):
    description = models.CharField(max_length=200)
    alarm_time_at = models.DateTimeField(db_index=True)

    def __str__(self):
        return self.description


@receiver(models.signals.post_save, sender=Alarm, dispatch_uid='alarm_save')
def poll_edit(sender, instance, using, **kwargs):
    now = datetime.datetime.now()
    if instance.alarm_time_at < now:
        return
    set_an_alarm.apply_async(args=[instance.description], eta=instance.alarm_time_at)
