from django_filters import rest_framework as filters, ModelChoiceFilter
from api.doctors.services import SubServiceService
from api.cities.services import CityService


class ClinicFilter(filters.FilterSet):
    city = ModelChoiceFilter(queryset=CityService.filter(is_deleted=False))
    subservice_clinic = ModelChoiceFilter(queryset=SubServiceService.filter(is_deleted=False))

# class ClinicFilter(filters.FilterSet):
#     city = ModelChoiceFilter(queryset=City.objects.all())
#     subservice_clinic = ModelChoiceFilter(queryset=SubService.objects.all())
