from enum import unique

from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import GroupEvent, SendNotice
from .serializers import (
    GroupEventSerializer,
    SendNoticeSerializer,
    SubscribeUserOnPushSerializer,
)


class GroupsEventsView(generics.ListAPIView):
    """
    Список группы событий
    """

    serializer_class = GroupEventSerializer
    permission_classes = [IsAuthenticated]
    queryset = GroupEvent.objects.all()


class SendNoticeListAPIView(generics.ListAPIView):
    """
    Список уведомлений
    """

    serializer_class = SendNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SendNotice.objects.filter(user_id=user.pk).order_by(
            "notice__event__priority", "date_of_send"
        )
        return queryset


class SendNoticeRetrieveAPIView(generics.RetrieveAPIView):
    """
    Детальный обзор уведомления
    """

    serializer_class = SendNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SendNotice.objects.filter(user_id=user.pk)
        return queryset


class AllGroupNoticeList(generics.ListAPIView):
    """Отображение списка всех групп уведомлений  имеющихся у пользователя """

    serializer_class = SendNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SendNotice.objects.filter(user_id=user.pk)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data

        # получение списка групп
        group_notice = []
        for item in response_list:
            group_notice.append(dict(item["notice"]["event"]["group"]))

        # удаление повторов в списке объектов
        seen_names = set()
        unique_group_notice = []
        for item in group_notice:
            if item["name"] not in seen_names:
                unique_group_notice.append(item)
                seen_names.add(item["name"])

        # добавление поля count
        for item in unique_group_notice:
            item.update({"count": 0})

        # подсчет количества уведомлений в каждой группе
        for item_unique in unique_group_notice:
            for item in group_notice:
                if item_unique["id"] == item["id"]:
                    item_unique["count"] += 1

        return Response(unique_group_notice)


class NoticeOfOneGroupNoticeList(generics.ListAPIView):
    """ Список уведомления пользователя для выбранной группы уведомлений """

    lookup_url_kwarg = "group"
    serializer_class = SendNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SendNotice.objects.filter(user_id=user.pk)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data
        group = self.kwargs["group"]
        list_result = []
        for item in response_list:
            if item["notice"]["event"]["group"]["id"] == group:
                list_result.append(item)
        return Response(list_result)


class SubscribeOnPush(generics.UpdateAPIView):
    serializer_class = SubscribeUserOnPushSerializer

    def get_queryset(self):
        queryset = get_user_model().objects.all()
        return queryset
