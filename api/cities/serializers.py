from rest_framework import serializers
from api.cities import models


class CitySerializer(serializers.ModelSerializer):
    """Города"""

    class Meta:
        model = models.City
        fields = (
            "id",
            "slug",
            "created_at",
            "name",
        )
