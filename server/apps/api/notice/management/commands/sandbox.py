from django.core.management.base import BaseCommand
from apps.api.notice.models import GroupEvent
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'this sandbox command'

    def handle(self, *args, **options):
        ge = GroupEvent.objects.first()
        print(ge.get_l_count(user=get_user_model().objects.first()))

