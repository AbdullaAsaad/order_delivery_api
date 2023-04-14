from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet, DeliveryAgentViewSet, OrderViewSet


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'delivery_agents', DeliveryAgentViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
   path('', include(router.urls)),
]