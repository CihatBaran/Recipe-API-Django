from user.serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.exceptions import ValidationError


class CreateUserView(CreateAPIView):
    """Create a new user to the system """

    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        password = request.data.get('password')
        if (len(password) < 5):
            raise ValidationError(
                {'password': "Password should be at least 5 chars"})

        return super().create(request, *args, **kwargs)
