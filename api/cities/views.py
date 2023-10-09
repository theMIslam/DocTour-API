from rest_framework import generics
from api.cities import models, serializers


class CityAPIView(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
