from django.urls import path

from .views import SendNoticeListAPIView

app_name = "notice"

urlpatterns = [
    path("list/", SendNoticeListAPIView.as_view()),
]
