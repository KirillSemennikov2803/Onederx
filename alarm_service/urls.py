from django.urls import path

from alarm_service.views import add_alarm, get_alarm_list

app_name = "alarm_service"

urlpatterns = [
    path('add', add_alarm.UserView().as_view()),
    path('get', get_alarm_list.UserView.as_view())
]
