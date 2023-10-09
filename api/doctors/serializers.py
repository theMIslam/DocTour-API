from rest_framework import serializers
from django.db.models import Avg
from api.doctors import constants, validators
from api.doctors import models
from api.clinics.serializers import ClinicsSerializer
from api.docdetail import serializers as docserializers


class FavoriteDoctorSerializer(serializers.ModelSerializer):
    doctor_data = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()

    class Meta:
        model = models.FavoriteDoctors
        exclude = ("user",)

    def get_doctor_data(self, obj):
        return obj.doctor.full_name

    def get_user_data(self, obj):
        return obj.user.fullname


class FavoriteClinicSerializer(serializers.ModelSerializer):
    clinics_data = serializers.SerializerMethodField()
    user_data = serializers.SerializerMethodField()

    class Meta:
        model = models.FavoriteClinics
        exclude = ("user",)

    def get_clinics_data(self, obj):
        return obj.clinics.title

    def get_user_data(self, obj):
        return obj.user.fullname


class SpecialitySerializer(serializers.ModelSerializer):
    """Специальности"""

    doctors_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Speciality
        fields = (
            "id",
            "slug",
            "name",
            "doctors_count",
        )

    def get_doctors_count(self, obj):
        return obj.doctors_specialties.count()


class SubServiceSerializer(serializers.ModelSerializer):
    """Под Услуги"""

    clinic = ClinicsSerializer(many=True, write_only=True)
    count_clinic = serializers.SerializerMethodField()

    class Meta:
        model = models.SubService
        fields = (
            "id",
            "name",
            "slug",
            "count_clinic",
            "service",
            "clinic",
        )

    def get_count_clinic(self, obj):
        return obj.clinic.count()


class ServiceSerializer(serializers.ModelSerializer):
    """Услуги"""

    subservice_service = SubServiceSerializer(many=True)

    class Meta:
        model = models.Service
        fields = (
            "slug",
            "name",
            "subservice_service",
        )


class ReviewSerializer(serializers.ModelSerializer):
    doctor_name = serializers.SerializerMethodField()
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Review
        fields = (
            'id',
            'text',
            'stars',
            'doctor',
            'user_name',
            'doctor_name',
            'created_at'
        )
        read_only_fields = (
            'id',
            'created_at'
        )

    def get_doctor_name(self, review):
        return review.doctor.full_name

    def get_user_name(self, review):
        return review.user.fullname


class SpecialitySerializerFields(SpecialitySerializer):
    class Meta:
        model = models.Speciality
        fields = ('slug', 'name')


class DoctorSerializer(serializers.ModelSerializer):
    """Главный список врачей"""

    average_rating = serializers.SerializerMethodField()
    num_reviews = serializers.SerializerMethodField()
    specialties = SpecialitySerializerFields(many=True, read_only=True)
    clinic = ClinicsSerializer(many=True, read_only=True)

    class Meta:
        model = models.Doctor
        fields = (
            "id",
            "full_name",
            "photo",
            "summary",
            "experience",
            "price",
            "instagram",
            "average_rating",
            "num_reviews",
            "specialties",
            "clinic",
        )

    def get_average_rating(self, obj):
        return obj.doctor_reviews.aggregate(avg_rating=Avg("stars"))["avg_rating"]

    def get_num_reviews(self, obj):
        return obj.doctor_reviews.count()


class DoctorDetailSerializer(DoctorSerializer):
    doctor_experience = docserializers.ExperienceSerializer(many=True)
    doctor_certificates = docserializers.CertificatesSerializer(many=True)
    doctor_education = docserializers.EducationSerializer(many=True)
    doctor_specialization = docserializers.SpecializationSerializer(many=True)
    doctor_reviews = ReviewSerializer(many=True)
    clinic = ClinicsSerializer(many=True)


    class Meta:
        model = models.Doctor
        fields = "__all__"


class WhatsappSendSerializer(serializers.Serializer):
    """Запись к врачу"""

    doctor = serializers.PrimaryKeyRelatedField(queryset=models.Doctor.objects.all())
    fullname = serializers.CharField()
    birthday = serializers.DateField()
    gender = serializers.ChoiceField(choices=constants.GENDER)
    phone_number = serializers.CharField(validators=[validators.PhoneValidator])

    def get_doctor_phone(self, validated_data):
        doctor_serializer = DoctorDetailSerializer(validated_data.get("doctor"))
        return doctor_serializer.data.get("phone")

    def create(self, validated_data):
        return validated_data
