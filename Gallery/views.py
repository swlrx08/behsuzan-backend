from rest_framework.viewsets import ModelViewSet
from .models import Gallery
from .serializers import GallerySerializer


class GalleryImageViewSet(ModelViewSet):
    queryset = Gallery.objects.all().order_by('-uploaded_at')
    serializer_class = GallerySerializer
