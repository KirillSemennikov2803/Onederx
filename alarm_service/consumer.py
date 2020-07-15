import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class AlarmConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            "alarm",
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            "alarm",
            self.channel_name
        )

    def alarm(self, event):
        message = event['message']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
