from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    """
    Модель события
    """

    PRIORITY_CHOICES = [
        ("low", "Низкий приоритет"),
        ("middle", "Средний приоритет"),
        ("high", "Высокий приоритет"),
    ]

    title = models.CharField(_("Заголовок"), max_length=255, null=True)
    priority = models.CharField(
        _("Приоритет"), max_length=50, choices=PRIORITY_CHOICES
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Notice(models.Model):
    """
    Модель уведомления
    """

    event = models.ForeignKey(
        Event,
        verbose_name=_("Событие"),
        on_delete=models.CASCADE,
    )
    number_version = models.IntegerField(_("Номер версии уведомления"))
    desc_version = models.CharField(
        _("Описание отличия версии"), max_length=150
    )
    text = models.CharField(
        _("Основной текст"),
        max_length=350,
        null=True,
    )
    img = models.ImageField(_("Картинка"), upload_to="notice-img")

    def __str__(self):
        return f"{self.event} {self.number_version}"

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class SendNotice(models.Model):
    """
    Модель отправки уведомления пользователю
    """

    user = models.ForeignKey(
        get_user_model(),
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
    )
    notice = models.ForeignKey(
        Notice,
        verbose_name=_("Отпарвленное уведомление"),
        on_delete=models.CASCADE,
    )

    date_of_send = models.DateField(
        _("Дата отправки"),
        default=timezone.now,
    )

    def __str__(self):
        return f"{self.user} {self.notice}"

    class Meta:
        verbose_name = "Отправка уведомления"
        verbose_name_plural = "Отправка уведомления"
