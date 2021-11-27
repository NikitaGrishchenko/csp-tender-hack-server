from django.urls import path

from .views import SendNoticeListAPIView, SendNoticeRetrieveAPIView, GroupsEventsView

app_name = "notice"

urlpatterns = [
    path("groups-events/", GroupsEventsView.as_view()),
    path("list/", SendNoticeListAPIView.as_view()),
    path("detail/<int:pk>/", SendNoticeRetrieveAPIView.as_view()),
]
