from user.serializers import UserSerializer, AuthTokenSerializer

from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework import authentication
from rest_framework import permissions


class CreateUserView(CreateAPIView):
    """Create a new user to the system """

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')
        if (len(password) < 5):
            raise ValidationError(
                {'password': "Password should be at least 5 chars"})

        return super().create(request, *args, **kwargs)


class CreateTokenView(ObtainAuthToken):
    """Create new authtoken for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(RetrieveUpdateAPIView):
    """Manage authenticated user.."""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
