from django.urls import path
from api.doctors import views

urlpatterns = [
    path("favorites-doctors/", views.FavoriteDoctorsListCreateAPIView.as_view()),
    path("favorites-doctors/<int:id>/", views.FavoriteDoctorRetrieveDeleteAPIView.as_view()),
    path("favorites-clinics/", views.FavoriteClinicListCreateAPIView.as_view()),
    path("favorites-clinics/<int:id>/", views.FavoriteClinicRetrieveDeleteAPIView.as_view()),
    path("doctors/", views.DoctorListAPIView.as_view(), name="Врачи"),
    path("doctors/<str:id>/", views.DoctorDetailAPIView.as_view(), name="Врачи по ID"),
    path("reviews/", views.ReviewListAPIView.as_view(), name="Отзывы"),
    path("speciality/", views.SpecialityAPIView.as_view(), name="Специальности"),
    path("service/", views.ServiceAPIView.as_view(), name="Услуги"),
    path(
        "sub-service/",
        views.SubServiceClinicsAPIView.as_view(),
        name="Под Услуги Клиники",
    ),
    path("whatsapp-send/", views.WhatsappSendView.as_view(), name="Запись к врачу"),
    path("search-by-city/<str:id>/", views.SearchAPIView.as_view()),
]
