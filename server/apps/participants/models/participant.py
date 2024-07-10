import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class Participant(BaseModel):
    """Модель для хранения участника тестирования"""

    name = models.CharField(max_length=255, verbose_name=_("Имя"))
    patronymic = models.CharField(
        max_length=255, blank=True, verbose_name=_("Отчество")
    )
    surname = models.CharField(max_length=255, verbose_name=_("Фамилия"))
    email = models.EmailField(blank=True, verbose_name=_("Электронная почта"))
    hh = models.CharField(
        max_length=255, blank=True, verbose_name=_("Ссылка на резюме")
    )

    class Meta:
        verbose_name = _("Участник")
        verbose_name_plural = _("Участники")

    def __str__(self):
        return self.name
