from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class Subscription(BaseModel):
    """Модель подписки"""
    title = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.CharField(max_length=100, verbose_name=_("Описание"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("Стоимость"))
    surveys_amount = models.PositiveIntegerField(default=0, verbose_name=_("Максимальное количество доступных тестов"))

    class Meta:
        verbose_name = _("Подписка")
        verbose_name_plural = _("Подписки")

    def __str__(self):
        return f'Название: {self.title}. Стоимость: {self.price}'
