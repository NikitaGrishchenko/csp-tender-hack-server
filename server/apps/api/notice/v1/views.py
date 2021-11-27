from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ..models import SendNotice
from .serializers import SendNoticeSerializer


class SendNoticeListAPIView(generics.ListAPIView):
    serializer_class = SendNoticeSerializer
    queryset = SendNotice.objects.all()
    permission_classes = [IsAuthenticated]
