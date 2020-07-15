from __future__ import absolute_import, unicode_literals

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer


@shared_task()
def set_an_alarm(alarm_des):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "alarm",
        {
            'type': 'alarm',
            'message': alarm_des
        })
