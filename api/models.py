from django.db import models
from geopy.distance import geodesic
import datetime

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DeliveryAgent(models.Model):
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

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.CASCADE)
    order_details = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)
    
    def __str__(self):
        return f'Order Nume #{self.id}'