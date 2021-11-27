from apps.core.utils.admin import BaseAdminMixin
from django.contrib.admin import ModelAdmin, register

from .models import Event, Notice, SendNotice, GroupEvent


@register(GroupEvent)
class GroupEventAdmin(ModelAdmin, BaseAdminMixin):
    """
    Админка групп событий
    """

    list_display = (
        "name",
    )


@register(Event)
class EventAdmin(ModelAdmin, BaseAdminMixin):
    """
    Админка события
    """

    list_display = (
        "title",
        "priority",
    )
    list_filter = ("priority",)


@register(Notice)
class NoticeAdmin(ModelAdmin, BaseAdminMixin):
    """
    Админка уведомления
    """

    list_display = (
        "event",
        "number_version",
    )
    list_filter = ("event",)


@register(SendNotice)
class SendNoticeAdmin(ModelAdmin, BaseAdminMixin):
    """
    Админка отправки уведомления
    """

    list_display = (
        "user",
        "notice",
        "date_of_send",
        "is_viewed",
        "is_archived",
    )
    list_filter = (
        "user",
        "notice",
        "is_viewed",
        "is_archived",
    )
