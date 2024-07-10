from rest_framework.serializers import ModelSerializer

from server.apps.companies.models.subscription import Subscription


class SubscriptionSerializer(ModelSerializer):
    """Serializer для подписки"""
    class Meta:
        model = Subscription
        fields = (
            'id',
            'title',
            'description',
            'price',
            'surveys_amount',
            'created',
            'updated',
        )
        read_only_fields = (
            'id',
            'created',
            'updated',
        )
