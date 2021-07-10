from .models import Order
from rest_framework.serializers import HyperlinkedModelSerializer


class OrderSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'url', 'customer', 'product', 'amount', 'date', 'status', 'created_at')