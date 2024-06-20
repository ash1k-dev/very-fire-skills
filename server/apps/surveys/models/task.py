from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class Task(BaseModel):
    """Модель тестового задания"""

    title = models.CharField(max_length=100, verbose_name=_("Название"))
    creator = models.ForeignKey(
        to="auth.User",
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name=_("Создатель"),
    )
    description = models.CharField(max_length=100, verbose_name=_("Описание"))
    text = models.CharField(max_length=100, blank=True, verbose_name=_("Текст"))
    survey = models.OneToOneField(
        to="surveys.Survey",
        on_delete=models.CASCADE,
        related_name="tasks",
        verbose_name=_("Опрос"),
    )

    class Meta:
        verbose_name = _("Задание")
        verbose_name_plural = _("Задания")

    def __str__(self):
        return self.title
