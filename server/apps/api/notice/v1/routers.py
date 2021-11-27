from django.urls import path

from .views import (
    AllGroupNoticeList,
    GroupsEventsView,
    NoticeOfOneGroupNoticeList,
    SendNoticeListAPIView,
    SendNoticeRetrieveAPIView,
)

app_name = "notice"

urlpatterns = [
    path("groups-events/", GroupsEventsView.as_view()),
    path("list/", SendNoticeListAPIView.as_view()),
    path("detail/<int:pk>/", SendNoticeRetrieveAPIView.as_view()),
    path("all-group/", AllGroupNoticeList.as_view()),
    path("for-group/<int:group>/", NoticeOfOneGroupNoticeList.as_view()),
]
