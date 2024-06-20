from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from server.apps.utils.permissions import IsStaffPermission
from server.apps.companies.api.serializers import SubscriptionSerializer
from server.apps.companies.models import Subscription
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class SubscriptionFilter(django_filters.FilterSet):
    """Фильтр для подписок"""
    class Meta:
        model = Subscription
        fields = {
            'title': ['exact', 'icontains'],
            'price': ['exact', 'icontains'],
        }


class SubscriptionViewSet(ModelViewSet):
    """ViewSet для подписок"""
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    search_fields = ["title"]
    ordering_fields = '__all__'
    filter_backends = [DjangoFilterBackend]
    filterset_class = SubscriptionFilter
    permission_classes = [IsAuthenticated, IsStaffPermission]

