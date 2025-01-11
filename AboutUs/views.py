from django.shortcuts import render
from rest_framework import viewsets

from AboutUs.models import AboutUs
from AboutUs.serializers import AboutUsSerializer


class AboutUsViewSet(viewsets.ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

