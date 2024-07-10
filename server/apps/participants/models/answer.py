from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from server.apps.services import BaseModel


class Answer(BaseModel):
    """Модель для ответов пользователя"""

    participant_survey = models.ForeignKey(
        to="participants.ParticipantSurvey",
        on_delete=models.CASCADE,
        related_name="answers",
        db_index=True,
        verbose_name=_("Связь участника и опроса"),
    )
    question = models.ForeignKey(
        to="surveys.Question",
        on_delete=models.CASCADE,
        related_name="answers",
        db_index=True,
        verbose_name=_("Вопрос"),
    )
    option = models.ForeignKey(
        to="surveys.Option",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name=_("Вариант ответа"),
    )

    class Meta:
        verbose_name = _("Ответ")
        verbose_name_plural = _("Ответы")
        constraints = [
            UniqueConstraint(
                fields=["participant_survey", "question"],
                name="unique_participant_survey_and_question",
            )
        ]
