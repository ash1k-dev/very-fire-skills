from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services import BaseModel


class Company(BaseModel):
    """Модель компании"""

    creator = models.ForeignKey(
        to="auth.User",
        on_delete=models.CASCADE,
        related_name="companies",
        verbose_name=_("Владелец"),
    )
    title = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.CharField(max_length=100, verbose_name=_("Описание"))
    used_surveys = models.IntegerField(
        default=0, verbose_name=_("Использованные опросы")
    )

    class Meta:
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")

    def __str__(self):
        return self.title
