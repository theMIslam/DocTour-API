from django.urls import path
from api.users import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", views.UserRegistrationView.as_view(), name="user-registration"),
    path("login/", views.UserLoginUserAPIView.as_view(), name="user-authorization"),
    path("confirm-user/", views.UserConfirmAPIView.as_view(), name="user-confirm"),
    path("login/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", views.LogoutAPIView.as_view(), name="user-logout"),
    # создание кода для востановления
    path(
        "reset-password-phone-number/",
        views.PasswordResetSearchUserAPIView.as_view(),
        name="search user and generate code",
    ),
    # подтверждение кода
    path(
        "reset-password-code/",
        views.PasswordResetTokenAPIView.as_view(),
        name="code",
    ),
    # создание нового пароля + code
    path(
        "reset-new-password/<int:code>/",
        views.PasswordResetNewPasswordAPIView.as_view(),
        name="new-password",
    ),
    path("profile/", views.ProfileAPIView.as_view(), name="profile-list"),
    path("profile/<str:id>/", views.ProfileDetailAPIView.as_view(), name="profile-update,delete"),
]
