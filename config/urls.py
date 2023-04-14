from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = yasg_schema_view(
   openapi.Info(
      title="Order and Delivery Platform API",
        default_version='v1',
        description="API for managing customers, delivery agents, and orders",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="aboody.asaad99@gmail.com"),
        license=openapi.License(name="Abdulla Asaad"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/jwt/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
