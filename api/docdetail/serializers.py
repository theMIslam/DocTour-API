from rest_framework import serializers
from api.docdetail import models


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certificates
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = "__all__"


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = "__all__"
