import json
import os

from django.conf import settings
from django.db.models import signals
from django.dispatch import receiver
from pywebpush import webpush

from .models import SendNotice


@receiver(signals.post_save, sender=SendNotice)
def send_push(instance, *args, **kwargs):
    print()
    webpush(
        subscription_info={
            "endpoint": instance.user.webpush.endpoint,
            "keys": {
                "p256dh": instance.user.webpush.key_secret,
                "auth": instance.user.webpush.key_auth,
            },
        },
        data=f"{instance.notice.event.title}\n{instance.notice.text}",
        vapid_private_key="al8PNtoc6B4kJ1Nncad_vMMMkZ6rLWkHyiujBlqSi38",
        vapid_claims={"sub": "mailto:pen.egor2002@gmail.com"},
    )
