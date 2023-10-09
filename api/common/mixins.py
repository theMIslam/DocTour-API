from api.doctors import models
from api.doctors import serializers
from django.db.models import Q
from api.cities.serializers import CitySerializer

class GlobalSearchMixin:
    def global_querylist(self, qeurylist, search):
        qeurylist = (
            {
                "queryset": models.City.objects.filter(Q(name__icontains=search)),
                "serializer_class": CitySerializer,
            },
            {
                "queryset": models.Speciality.objects.filter(Q(name__icontains=search)),
                "serializer_class": serializers.SpecialitySerializer,
            },
            {
                "queryset": models.Service.objects.filter(Q(name__icontains=search)),
                "serializer_class": serializers.ServiceSerializer,
            },
            {
                "queryset": models.Clinics.objects.filter(Q(title__icontains=search)),
                "serializer_class": serializers.ClinicsSerializer,
            },
            {
                "queryset": models.Doctor.objects.filter(
                    Q(full_name__icontains=search)
                ),
                "serializer_class": serializers.DoctorSerializer,
            },
            {
                "queryset": models.SubService.objects.filter(Q(name__icontains=search)),
                "serializer_class": serializers.SubServiceSerializer,
            },
        )

        return qeurylist
