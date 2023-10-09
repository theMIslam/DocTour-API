from django_filters import rest_framework as filters, ModelChoiceFilter
from api.doctors import services as doctor_services
from api.cities import services as city_services
from api.clinics import services as clinic_services


class DoctorFilter(filters.FilterSet):
    specialties = ModelChoiceFilter(queryset=doctor_services.SpecialityService.filter(is_deleted=False))
    category_services = ModelChoiceFilter(queryset=doctor_services.ServicesService.filter(is_deleted=False))
    city = ModelChoiceFilter(queryset=city_services.CityService.filter(is_deleted=False))


class ReviewFilter(filters.FilterSet):
    doctors = ModelChoiceFilter(queryset=doctor_services.DoctorService.filter(is_deleted=False))


class SubServiceFilter(filters.FilterSet):
    clinic = ModelChoiceFilter(queryset=clinic_services.ClinicService.filter(is_deleted=False))
    service = ModelChoiceFilter(queryset=doctor_services.ServicesService.filter(is_deleted=False))


class ServicesFilter(filters.FilterSet):
    name = ModelChoiceFilter(queryset=doctor_services.ServicesService.filter(is_deleted=False))
    price = filters.RangeFilter(field_name="price")
