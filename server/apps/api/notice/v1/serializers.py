from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Event, Notice, SendNotice

user = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор пользователя
    """

    class Meta:
        model = user
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор событий
    """

    class Meta:
        model = Event
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):
    """
    Сериализатор уведомлений
    """

    event = EventSerializer

    class Meta:
        model = Notice
        fields = "__all__"


class SendNoticeSerializer(serializers.ModelSerializer):
    """
    Сериализатор отправленных уведомлений
    """

    notice = NoticeSerializer()
    user = UserSerializer()

    class Meta:
        model = SendNotice
        fields = "__all__"
