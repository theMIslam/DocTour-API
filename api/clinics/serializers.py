from rest_framework import serializers
from api.clinics import models


class ClinicsSerializer(serializers.ModelSerializer):
    """Клиники"""

    class Meta:
        model = models.Clinics
        fields = "__all__"
