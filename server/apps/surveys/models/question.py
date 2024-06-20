from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class Question(BaseModel):
    """Модель вопроса"""
    creator = models.ForeignKey(to="auth.User", on_delete=models.CASCADE, related_name='questions', verbose_name=_("Создатель"))
    survey = models.ForeignKey(to="surveys.Survey", on_delete=models.CASCADE, related_name='questions', verbose_name=_("Тест"))
    text = models.CharField(max_length=100, verbose_name=_("Вопрос"))
    question_weight = models.IntegerField(default=1, verbose_name=_("Вес вопроса"))

    class Meta:
        verbose_name = _("Вопрос")
        verbose_name_plural = _("Вопросы")

    def __str__(self) -> str:
        return self.text
