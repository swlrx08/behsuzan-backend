from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Accounts.views import AdminViewSet, AdminLoginViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='admin')

urlpatterns = [
    path('admin_login/', AdminLoginViewSet.as_view(), name='admin_login'),
    path('', include(router.urls)),
]
