from rest_framework import generics
from .models import MapPoint
from .serializers import MapPointSerializer


class MapPointList(generics.ListAPIView):
    queryset = MapPoint.objects.all()
    serializer_class = MapPointSerializer


class MapPointCreate(generics.CreateAPIView):
    queryset = MapPoint.objects.all()
    serializer_class = MapPointSerializer
