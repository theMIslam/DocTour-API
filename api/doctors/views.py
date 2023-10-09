from urllib.parse import quote
from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status, pagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter, SearchFilter
from api.doctors import serializers, services, paginations, filters, models


class FavoriteDoctorsListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.FavoriteDoctors.objects.all()
    serializer_class = serializers.FavoriteDoctorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        favorite = models.FavoriteDoctors.objects.create(user_id=request.user.id,
                                                         doctor=serializer.validated_data["doctor"],)
        return Response(data={"data": self.serializer_class(favorite).data, "message": "ok"}, status=status.HTTP_200_OK)


class FavoriteDoctorRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.FavoriteDoctors.objects.all()
    serializer_class = serializers.FavoriteDoctorSerializer
    lookup_field = "id"


class FavoriteClinicListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.FavoriteClinics.objects.all()
    serializer_class = serializers.FavoriteClinicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        favorite = models.FavoriteClinics.objects.create(user_id=request.user.id,
                                                         clinics=serializer.validated_data["clinics"],)
        return Response(data={"data": self.serializer_class(favorite).data, "message": "ok"}, status=status.HTTP_200_OK)


class FavoriteClinicRetrieveDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = models.FavoriteClinics.objects.all()
    serializer_class = serializers.FavoriteDoctorSerializer
    lookup_field = "id"


class ServiceAPIView(generics.ListAPIView):
    """Категории услуг врачей"""

    queryset = services.ServicesService.filter(is_deleted=False)
    serializer_class = serializers.ServiceSerializer
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["name", "slug"]


class SubServiceClinicsAPIView(generics.ListAPIView):
    queryset = services.SubServiceService.filter(is_deleted=False)
    serializer_class = serializers.SubServiceSerializer
    filterset_class = filters.SubServiceFilter
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["name", "slug"]


class SpecialityAPIView(generics.ListAPIView):
    """Специальность врачей"""

    queryset = services.SpecialityService.filter(is_deleted=False)
    serializer_class = serializers.SpecialitySerializer
    pagination_class = paginations.ServicePagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = ["name", "slug"]


class DoctorListAPIView(generics.ListAPIView):
    """Список врачей )"""

    queryset = services.DoctorService.filter(is_deleted=False).order_by('created_at')
    serializer_class = serializers.DoctorSerializer
    pagination_class = paginations.DoctorPagination
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_class = filters.DoctorFilter
    search_fields = ["full_name"]
    ordering_fields = ["price"]


class DoctorDetailAPIView(generics.RetrieveAPIView):
    """Врачи по ID"""

    queryset = services.DoctorService.filter(is_deleted=False)
    serializer_class = serializers.DoctorDetailSerializer
    lookup_field = "id"


class ReviewListAPIView(generics.ListCreateAPIView):
    """Список отзывов к врачам"""

    queryset = services.ReviewService.filter(is_deleted=False).order_by('-created_at')
    serializer_class = serializers.ReviewSerializer
    pagination_class = pagination.PageNumberPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        OrderingFilter,
    ]
    ordering_fields = ["stars"]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = services.ReviewService.create(
            user=request.user.id,
            text=serializer.validated_data['text'],
            doctor=serializer.validated_data['doctor'],
            stars=serializer.validated_data['stars']
        )
        return Response(
            status=status.HTTP_200_OK,
            data={
                'data': serializers.ReviewSerializer(review).data,
                'message': 'OK'
            }
        )


class WhatsappSendView(generics.GenericAPIView):
    """Ватсап запись к врачу"""

    serializer_class = serializers.WhatsappSendSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            doctor_phone = serializer.get_doctor_phone(serializer.validated_data)

            fullname = serializer.validated_data.get("fullname")
            birthday = serializer.validated_data.get("birthday")
            gender = serializer.validated_data.get("gender")
            phone_number = serializer.validated_data.get("phone_number")

            message = (
                "Здравствуйте я из приложения DocTour \n"
                f" ФИО: {fullname}\n Год рождения: {birthday}"
                f"\n Пол: {gender}\n Телефон: {phone_number}"
            )
            encoded_message = quote(message)

            whatsapp_web_url = (
                f"https://api.whatsapp.com/send?phone={doctor_phone}"
                f"&text={encoded_message}"
            )

            return redirect(to=whatsapp_web_url)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchAPIView(generics.ListAPIView):
    pagination_class = None

    def get_queryset(self):
        return None

    def list(self, request, *args, **kwargs):
        doctors, clinics = services.SearchService.filter(
            q=self.request.query_params.get('q', None),
            city=self.kwargs['id']
        )

        data = [
            {'model': 'Доктора', 'result': serializers.DoctorSerializer(doctors, many=True).data},
            {'model': 'Клиники', 'result': serializers.ClinicsSerializer(clinics, many=True).data},
        ]

        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
