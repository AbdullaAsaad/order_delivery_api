from rest_framework import viewsets
from .models import Customer, DeliveryAgent, Order
from .serializers import  CustomerSerializer, DeliveryAgentSerializer, OrderSerializer
from rest_framework import permissions

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permissions_classes = (permissions.IsAuthenticated,)
            
class DeliveryAgentViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions_classes = (permissions.IsAuthenticated,)