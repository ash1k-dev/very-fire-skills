from django.contrib import admin

from server.apps.companies.models import Company, Subscription, CompanySubscription


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Панель управления компаниями"""
    list_display = ('id','creator','title', 'description')
    list_filter = ('creator', )
    search_fields = ('title', )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin[Subscription]):
    """Панель управления подписками"""
    list_display = ('id','title','price', 'surveys_amount')
    list_filter = ('title', )
    search_fields = ('title', )


@admin.register(CompanySubscription)
class CompanySubscriptionAdmin(admin.ModelAdmin[CompanySubscription]):
    """Панель управления подписками компании"""
    list_display = ('id','company', 'subscription')
    list_select_related = ['company', 'subscription']
    list_filter = ('company', 'subscription')
    search_fields = ('company__title', 'subscription__title')
