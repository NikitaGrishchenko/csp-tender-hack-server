from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class NoticeConfig(AppConfig):
    """Default app config"""

    name = "apps.api.notice"
    verbose_name = _("Рассылка")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import
