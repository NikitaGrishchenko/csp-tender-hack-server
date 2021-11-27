from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import SendNotice
from .serializers import SendNoticeSerializer


class SendNoticeListAPIView(generics.ListAPIView):
    """
    Список уведомлений
    """

    serializer_class = SendNoticeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = SendNotice.objects.filter(user_id=user.pk).order_by('notice__event__priority', 'date_of_send')
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
