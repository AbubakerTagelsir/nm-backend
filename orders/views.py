from .models import Order
from .serializers import OrderSerializer
from rest_framework import viewsets,permissions
# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)