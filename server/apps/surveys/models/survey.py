from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services import BaseModel


class Survey(BaseModel):
    """Модель опроса"""

    company = models.ForeignKey(
        to="companies.Company",
        on_delete=models.CASCADE,
        related_name="surveys",
        verbose_name=_("Компания"),
    )
    creator = models.ForeignKey(
        to="auth.User",
        on_delete=models.CASCADE,
        related_name="surveys",
        verbose_name=_("Создатель"),
    )
    title = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.CharField(max_length=100, verbose_name=_("Описание"))
    passing_score = models.PositiveIntegerField(
        default=0, verbose_name=_("Проходной балл")
    )
    vacancy = models.CharField(max_length=100, blank=True, verbose_name=_("Вакансия"))
    time_limit = models.DurationField(default=0, verbose_name=_("Время"))
    is_public = models.BooleanField(default=False, verbose_name=_("Опрос активен"))

    class Meta:
        verbose_name = _("Тест")
        verbose_name_plural = _("Тесты")

    def __str__(self) -> str:
        return self.title
