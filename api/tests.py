from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, DeliveryAgent, Order
from .serializers import CustomerSerializer, DeliveryAgentSerializer, OrderSerializer

class CustomerTests(APITestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', phone_number='1234567890', address='123 Main St')
        self.url = reverse('customer-detail', args=[self.customer.id])
        
    def test_get_customer(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, CustomerSerializer(self.customer).data)
        
    def test_update_customer(self):
        data = {'name': 'Jane Doe', 'phone_number':'0987654321', 'address': '456 Elm St'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer.refresh_from_db()
        self.assertEqual(self.customer.name, 'Jane Doe')
        self.assertEqual(self.customer.phone_number, '0987654321')
        self.assertEqual(self.customer.address, '456 Elm St')
        
    def test_delete_customer(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(id=self.customer.id).exists())
        
class DeliveryAgentTests(APITestCase):

    def setUp(self):
        self.delivery_agent = DeliveryAgent.objects.create(name='John Smith', email='john@example.com', phone_number='1234567890', availability=True, address='123 Main St')
        self.url = reverse('delivery-agent-detail', args=[self.delivery_agent.id])
        
    def test_get_delivery_agent(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, DeliveryAgentSerializer(self.delivery_agent).data)

    def test_update_delivery_agent(self):
        data = {'name': 'Jane Smith', 'email': 'jane@example.com', 'phone_number': '0987654321', 'availability': False, 'address': '456 Elm St'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.delivery_agent.refresh_from_db()
        self.assertEqual(self.delivery_agent.name, 'Jane Smith')
        self.assertEqual(self.delivery_agent.email, 'jane@example.com')
        self.assertEqual(self.delivery_agent.phone_number, '0987654321')
        self.assertEqual(self.delivery_agent.availability, False)
        self.assertEqual(self.delivery_agent.address, '456 Elm St')

    def test_delete_delivery_agent(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(DeliveryAgent.objects.filter(id=self.delivery_agent.id).exists())

class OrderTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name='John Doe', phone_number='1234567890', address='123 Main St')
        self.delivery_agent = DeliveryAgent.objects.create(name='John Smith', email='john@example.com', phone_number='1234567890', availability=True, address='123 Main St')
        self.order = Order.objects.create(customer=self.customer, delivery_address='456 Elm St', order_details='Test Order Details')
        self.url = reverse('order-detail', args=[self.order.id])

    def test_get_order(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, OrderSerializer(self.order).data)

    def test_update_order(self):
        data = {'customer': self.customer.id, 'delivery_address': '789 Oak St', 'order_details': 'Updated Order Details'}
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order.refresh_from_db()
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.delivery_address, '789 Oak St')
        self.assertEqual(self.order.order_details, 'Updated Order Details')

    def test_delete_order(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order.id).exists())