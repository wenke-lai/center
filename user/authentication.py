from django.http import HttpRequest
from ninja.errors import AuthenticationError, AuthorizationError
from ninja.security import HttpBearer

from . import clerk
from .models import User


def is_signed_in(request: HttpRequest) -> str:
    try:
        if clerk_id := clerk.is_signed_in(request):
            return clerk_id
        raise AuthenticationError()
    except Exception:
        raise AuthenticationError()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            clerk_id = is_signed_in(request)
            return User.objects.get(clerk_id=clerk_id)
        except User.DoesNotExist:
            raise AuthorizationError()
