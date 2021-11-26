from rest_framework import serializers

from ..models import Event, Notice, SendNotice


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

    notice = NoticeSerializer

    class Meta:
        model = SendNotice
        fields = "__all__"
