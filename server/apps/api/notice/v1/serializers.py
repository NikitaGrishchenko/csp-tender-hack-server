from apps.api.auth.models import WebPushSubscription
from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..models import Event, GroupEvent, Notice, SendNotice

user = get_user_model()


class WebPushSubscriptionSerializer(serializers.ModelSerializer):
    """
    Сериализатор информации о подписке на Push
    """

    class Meta:
        model = WebPushSubscription
        fields = "__all__"


class SubscribeUserOnPushSerializer(serializers.ModelSerializer):
    """
    Сериализатор подписки пользователя на Push
    """

    webpush = WebPushSubscriptionSerializer()

    class Meta:
        model = user
        fields = [
            "webpush",
        ]


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


class GroupEventSerializer(serializers.ModelSerializer):
    """
    Сериализатор групп событий
    """

    class Meta:
        model = GroupEvent
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    """
    Сериализатор событий
    """

    group = GroupEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = "__all__"


class NoticeSerializer(serializers.ModelSerializer):
    """
    Сериализатор уведомлений
    """

    event = EventSerializer(read_only=True)

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


class GroupEventSerializer(serializers.ModelSerializer):
    """
    Сериализатор отправленных уведомлений
    """

    l = serializers.SerializerMethodField()
    m = serializers.SerializerMethodField()
    h = serializers.SerializerMethodField()

    class Meta:
        model = GroupEvent
        fields = "__all__"

    def get_l(self, obj):
        return obj.get_l_count(self.context["request"].user)

    def get_m(self, obj):
        return obj.get_m_count(self.context["request"].user)

    def get_h(self, obj):
        return obj.get_h_count(self.context["request"].user)
