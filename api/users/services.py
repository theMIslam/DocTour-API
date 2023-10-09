from rest_framework_simplejwt.tokens import RefreshToken
from api.common.services import Service
from api.users import models


class ConfirmCodeService(Service):
    model = models.UserConfirm


class ResetTokenService(Service):
    model = models.PasswordResetToken


class UserService(Service):
    model = models.User

    @staticmethod
    def get_token(user):
        refresh = RefreshToken.for_user(user)
        token = {"refresh": str(refresh), "access": str(refresh.access_token)}
        return token

    @classmethod
    def check_code(cls, code):
        if ConfirmCodeService.filter(code=code):
            cls.model.objects.update(is_active=True)
            ConfirmCodeService.filter(code=code).delete()
            return True
        else:
            return False
