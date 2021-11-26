from rest_framework import generics

from ..models import SendNotice
from .serializers import SendNoticeSerializer


class SendNoticeListAPIView(generics.ListAPIView):
    serializer_class = SendNoticeSerializer
    queryset = SendNotice.objects.all()
