from .models import Customer
from rest_framework.serializers import HyperlinkedModelSerializer


class CustomerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_name', 'photo', 'email', 'phone']