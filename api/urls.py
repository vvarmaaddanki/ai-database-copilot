from rest_framework.routers import DefaultRouter
from .views import DatabaseConnectionViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'database-connections', DatabaseConnectionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/login/", obtain_auth_token, name="api-token"),
]


