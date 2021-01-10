import base64
import binascii
from starlette.authentication import (
    AuthenticationBackend,
    BaseUser,
    AuthCredentials,
    UnauthenticatedUser,
    AuthenticationError,
)


class AuthenticatedUser(BaseUser):
    def __init__(self, email):
        self.email = email

    # def __init__(self, id, email):
    #     self.id = id
    #     self.email = email

    @property
    def is_authenticated(self):
        return True

    @property
    def display_name(self) -> str:
        return self.email


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(self, request):
        user = UnauthenticatedUser()
        if "Authorization" not in request.headers:
            return

        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return
            decoded = base64.b64decode(credentials).decode("ascii")
        except (ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        email, _, password = decoded.partition(":")
        print("==================")
        user = AuthenticatedUser(email)

        # verified_user = authenticaticate_user(email, password)
        # if verified_user:
        # user = AuthenticatedUser(verified_user.id, verified_user.email)
        return AuthCredentials(["authenticated"]), user