from django.db import models
from django.conf import settings
import uuid


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True,on_delete=models.CASCADE,  related_name="customer_users")
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
        
    def __str__(self):
        return self.name

class DeliveryAgent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_index=True,on_delete=models.CASCADE , related_name="delivery_agent_users")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    PENDING = 'P'
    ASSIGNED = 'A'
    DELIVERED = 'D'
    CANCELLED = 'C'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ASSIGNED, 'Assigned'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.CASCADE)
    order_details = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return f'Order Nume #{self.id}'