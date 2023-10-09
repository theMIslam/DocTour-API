from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics
from api.clinics import paginations, services, serializers, filters


class ClinicsAPIView(generics.ListAPIView):
    """Клиники"""

    queryset = services.ClinicService.filter(is_deleted=False)
    serializer_class = serializers.ClinicsSerializer
    pagination_class = paginations.ClinicPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    filterset_class = filters.ClinicFilter
    search_fields = ["title", "address"]
