from api.docdetail import models
from api.common.services import Service


class EducationService(Service):
    model = models.Education


class ExperienceService(Service):
    model = models.Experience


class CertificatesService(Service):
    model = models.Certificates


class SpecializationService(Service):
    model = models.Specialization

