from django.urls import path

from .views import SendNoticeListAPIView, SendNoticeRetrieveAPIView

app_name = "notice"

urlpatterns = [
    path("list/", SendNoticeListAPIView.as_view()),
    path("detail/<int:pk>/", SendNoticeRetrieveAPIView.as_view()),
]
