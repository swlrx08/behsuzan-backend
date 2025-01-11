from rest_framework.viewsets import ModelViewSet
from .models import ContactUs
from .serializers import ContactUsSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_read']
