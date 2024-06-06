from rest_framework import viewsets
from .models import Part
from .serializers import PartSerializer


class PartViewSet(viewsets.ModelViewSet):
    """
    ModelViewset provides the standard CRUD actions
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer
