from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.services import BaseModel


class Option(BaseModel):
    """Модель варианта ответа на вопрос"""

    creator = models.ForeignKey(
        to="auth.User",
        on_delete=models.CASCADE,
        related_name="answers",
        verbose_name=_("Пользователь"),
    )
    question = models.ForeignKey(
        to="surveys.Question",
        on_delete=models.CASCADE,
        related_name="options",
        db_index=True,
        verbose_name=_("Вопрос"),
    )
    text = models.CharField(max_length=100, verbose_name=_("Вариант ответа"))
    is_correct = models.BooleanField(
        default=False, verbose_name=_("Ответ является правильным")
    )

    class Meta:
        verbose_name = _("Вариант ответа")
        verbose_name_plural = _("Варианты ответа")
        constraints = [
            models.UniqueConstraint(
                fields=["question", "text"], name="unique_question_and_text"
            )
        ]

    def __str__(self) -> str:
        return self.text
