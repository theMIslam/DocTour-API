from django.urls import path
from api.clinics import views


urlpatterns = [
    path("clinics/", views.ClinicsAPIView.as_view(), name="Клиники"),
]
