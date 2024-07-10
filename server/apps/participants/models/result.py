from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class Result(BaseModel):
    """Модель результата теста"""
    participant_survey = models.OneToOneField(to='participants.ParticipantSurvey', related_name='results', on_delete=models.CASCADE, verbose_name=_("Связь участника и опроса"))
    result = models.PositiveIntegerField(default=0, verbose_name=_("Результат"))
    is_send_task = models.BooleanField(default=False, blank=True, null=True, verbose_name=_("Отправлено задание"))

    class Meta:
        verbose_name = _("Результат")
        verbose_name_plural = _("Результаты")

    def __str__(self):
        return str(self.result)



