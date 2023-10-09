from api.doctors import models
from api.common.services import Service
from api.clinics.services import ClinicService
from django.db.models import Q, F
from functools import reduce
from operator import or_


class SpecialityService(Service):
    model = models.Speciality


class ServicesService(Service):
    model = models.Service


class SubServiceService(Service):
    model = models.SubService


class DoctorService(Service):
    model = models.Doctor


class ReviewService(Service):
    model = models.Review

    @classmethod
    def create(cls, user, text, doctor, stars):
        return cls.model.objects.create(
            user_id=user,
            text=text,
            doctor=doctor,
            stars=stars
        )


class SearchService:
    @classmethod
    def get_filters(cls, view, fields):
        search_term = view.request.GET.get(view.search_keyword_arg, '')
        return reduce(or_, [Q(**{f'{field}__{view.lookup_expr}': search_term})
                            for field in fields])

    @classmethod
    def filter(cls, q, city):
        if q == None or len(q) < 3:
            return [], []

        doctors = DoctorService.filter(Q(full_name__icontains=q),
                                       city_id=city)[:8]
        clinics = ClinicService.filter(Q(title__icontains=q),
                                       city_id=city)[:8]

        return doctors, clinics
