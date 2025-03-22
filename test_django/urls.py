# test_django/urls.py

from django.contrib import admin
from django.urls import path, include
from events.views_user import UserRegistrationView  # Імпортуємо новий view
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from events.views import EventViewSet, EventRegistrationView

# Створюємо view для Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Event Management API",
        default_version='v1',
        description="API для управління подіями",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@eventapi.local"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Роутер для подій
router = DefaultRouter()
router.register(r'events', EventViewSet)  # для подій

# URL маршрути для проекту
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='register'),  # Для реєстрації
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Токен
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Оновлення токену
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('api/register_event/', EventRegistrationView.as_view(), name='register_event'),
]
