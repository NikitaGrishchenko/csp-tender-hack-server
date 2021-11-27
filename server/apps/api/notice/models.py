from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class GroupEvent(models.Model):
    """
    Группа событий
    """

    name = models.CharField(_("Наименование"), max_length=255, null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Группа событий'
        verbose_name_plural = 'Группы событий'


class Event(models.Model):
    """
    Модель события
    """

    PRIORITY_CHOICES = [
        (1, "Низкий приоритет"),
        (2, "Средний приоритет"),
        (3, "Высокий приоритет"),
    ]

    title = models.CharField(_("Заголовок"), max_length=255, null=True)
    priority = models.IntegerField(
        _("Приоритет"), choices=PRIORITY_CHOICES
    )

    group = models.ForeignKey(GroupEvent, related_name='events', on_delete=models.SET_NULL, blank=True, null=True)

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
    img = models.ImageField(
        _("Картинка"), upload_to="notice-img", null=True, blank=True
    )

    def __str__(self):
        return f"{self.event} {self.number_version}"

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"


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
        verbose_name=_("Отправленное уведомление"),
        on_delete=models.CASCADE,
    )

    date_of_send = models.DateTimeField(
        _("Дата отправки"),
        default=timezone.now,
    )

    date_of_execution = models.DateTimeField(
        _("Дата исполнения"), null=True, blank=True
    )

    is_viewed = models.BooleanField(_("Являеется просмотренным"), default=False)
    is_archived = models.BooleanField(_("Являеется архивным"), default=False)

    def __str__(self):
        return f"{self.user} {self.notice}"

    class Meta:
        verbose_name = "Отправка уведомления"
        verbose_name_plural = "Отправка уведомления"
