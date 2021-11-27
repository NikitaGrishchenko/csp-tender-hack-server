from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("notice/", include("apps.api.notice.v1")),
    path("auth/", include("apps.api.auth.v1")),
]
