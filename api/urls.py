from django.urls import include, path
from rest_framework import routers
from .views import CustomerViewSet, DeliveryAgentViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'delivery_agents', DeliveryAgentViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
   path('', include(router.urls)),
   #  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   #  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   #  path('custom-users/', CustomUserList.as_view(), name='custom_user_list'),
   #  path('custom-users/<int:pk>/', CustomUserDetail.as_view(), name='custom_user_detail'),
]