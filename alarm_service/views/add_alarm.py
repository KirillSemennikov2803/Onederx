import json

from rest_framework.views import APIView

from main_function.datatime_function import jsts_2_python_datetime
from main_function.response_processing import server_error_response, validate_response
from ..models import Alarm
from main_function.request_validation import validate_request

with open('alarm_service/schemas/add_alarm/req_schema.json', 'r') as f:
    schema_data = f.read()
req_schema = json.loads(schema_data)

with open('alarm_service/schemas/add_alarm/res_schema.json', 'r') as f:
    schema_data = f.read()
res_schema = json.loads(schema_data)


class UserView(APIView):
    @validate_request(req_schema)
    def post(self, request):
        try:
            description = request.data["description"]
            alarm_time = request.data["alarmTime"]

            alarm_time = jsts_2_python_datetime(alarm_time)
            Alarm.objects.create(description=description, alarm_time_at=alarm_time)

            return validate_response({"status": "ok"}, res_schema)
        except Exception as error:
            print(error)
            return server_error_response()
