import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class ParticipantSurvey(BaseModel):
    """Модель связывающая участника и опрос"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, verbose_name=_("UUID"))
    creator = models.ForeignKey(to='auth.User', related_name='participant_surveys', on_delete=models.CASCADE, db_index=True, verbose_name=_("Создатель"))
    participant = models.ForeignKey(to='participants.Participant', related_name='participants', on_delete=models.CASCADE, db_index=True, verbose_name=_("Участник"))
    survey = models.ForeignKey(to='surveys.Survey', related_name='participants', on_delete=models.CASCADE, db_index=True, verbose_name=_("Опрос"))

    class Meta:
        verbose_name = _("Участник и опрос")
        verbose_name_plural = _("Участники и опросы")
        constraints = [
            UniqueConstraint(fields=['participant', 'survey'], name='unique_participant_and_survey')
        ]

    def __str__(self):
        return f"Участник: {self.participant}. Опрос: {self.survey}"
