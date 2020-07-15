import json
from datetime import datetime

from rest_framework.views import APIView

from main_function.datatime_function import jsts_2_python_datetime, python_datetime_2_jsts
from main_function.response_processing import server_error_response, validate_response
from ..models import Alarm
from main_function.request_validation import validate_request


with open('alarm_service/schemas/get_alarm_list/res_schema.json', 'r') as f:
    schema_data = f.read()
res_schema = json.loads(schema_data)


class UserView(APIView):
    def get(self, request):
        try:
            now = datetime.now()
            alarms = Alarm.objects.filter(alarm_time_at__gte=now)
            res_alarms_data = []

            for alarm in alarms:
                alarm_time = python_datetime_2_jsts(alarm.alarm_time_at)
                res_alarms_data.append({"description": alarm.description,
                                        "alarmTime": alarm_time})

            return validate_response({"alarms": res_alarms_data}, res_schema)
        except Exception as error:
            print(error)
            return server_error_response()
