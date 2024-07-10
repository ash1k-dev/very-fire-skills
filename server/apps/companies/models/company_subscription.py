from django.db import models
from django.utils.translation import gettext_lazy as _

from server.apps.utils import BaseModel


class CompanySubscription(BaseModel):
    """Модель подписки компании"""
    company = models.ForeignKey(to='companies.Company', on_delete=models.CASCADE, related_name='company_subscriptions', verbose_name=_("Компания"))
    subscription = models.ForeignKey(to='companies.Subscription', on_delete=models.CASCADE, related_name='company_subscriptions', verbose_name=_("Подписка"))


    class Meta:
        verbose_name = _("Подписка компании")
        verbose_name_plural = _("Подписки компании")

    def __str__(self):
        return f"Компания: {self.company}. Подписка: {self.subscription}"
