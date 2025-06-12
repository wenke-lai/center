import logging

from ninja import Router
from ninja.errors import AuthenticationError, AuthorizationError

from .clerk import get_clerk_user, is_signed_in
from .models import User

logger = logging.getLogger(__name__)

router = Router()


@router.get("/onboarding")
def onboarding(request):
    if clerk_id := is_signed_in(request):
        if User.objects.filter(clerk_id=clerk_id).exists():
            return {"detail": "done"}
        else:
            clerk_user = get_clerk_user(user_id=clerk_id)
            User.objects.create(
                clerk_id=clerk_id,
                username=clerk_user.username,
            )
            return {"detail": "created"}
    raise AuthenticationError()


@router.get("/me")
def me(request):
    # for test
    if clerk_id := is_signed_in(request):
        try:
            user = User.objects.get(clerk_id=clerk_id)
            logger.info("user is onboarded, %s, %s", clerk_id, user.id)
            return {"detail": "ok"}
        except User.DoesNotExist:
            logger.error("user is not onboarded, %s", clerk_id)
            raise AuthorizationError()
    logger.error("invalid auth bearer, %s", request.headers.get("Authorization"))
    raise AuthenticationError()
