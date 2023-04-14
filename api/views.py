from rest_framework import viewsets, permissions
from .models import Customer, DeliveryAgent, Order
from .serializers import CustomerSerializer, DeliveryAgentSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import datetime
from geopy.distance import geodesic

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
        
class DeliveryAgentViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]   
     
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated] 
    
    def perform_create(self, serializer):
        customer = self.request.user
        delivery_agents = DeliveryAgent.objects.filter(availability=True)
        closest_agent = None
        min_distance = float("inf")

        for agent in delivery_agents:
            distance = self.calculate_distance(customer.address, agent.address)
            if distance < min_distance:
                min_distance = distance
                closest_agent = agent

        if closest_agent:
            serializer.save(customer=customer, status="Assigned")
        else:
            serializer.save(customer=customer, status="Pending")
            
    def calculate_distance(self):
        if self.delivery_agent.availability==True:
            delivery_address= self.delivery_agent.address
            customer_address= self.customer.address
            distance = geodesic(delivery_address, customer_address).km
            if(distance>5):
                return "this order is out zone of the delivery"
            elif(distance <5 and distance>4):
                time_taken = datetime.timedelta(minutes=40)
                timestamp = datetime.datetime.now() + time_taken
                return f"the distance is:{distance}km and this order is took time {timestamp}."
            elif(distance <4 and distance>3):
                time_taken = datetime.timedelta(minutes=30)
                timestamp = datetime.datetime.now() + time_taken
                return f"the distance is:{distance}km and this order is took time {timestamp}."
            elif(distance <3 and distance>2):
                time_taken = datetime.timedelta(minutes=20)
                timestamp = datetime.datetime.now() + time_taken
                return f"the distance is:{distance}km and this order is took time {timestamp}."
            else:
                time_taken = datetime.timedelta(minutes=15)
                timestamp = datetime.datetime.now() + time_taken
                return f"the distance is:{distance}km and this order is took time {timestamp}."
    