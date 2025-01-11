from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet

router = DefaultRouter()
router.register('', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
