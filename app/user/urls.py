from django.urls import path
from user.api_views import CreateUserView, CreateTokenView

app_name = 'user'

urlpatterns = [
    path('new/', CreateUserView.as_view(), name="create"),
    path('token/', CreateTokenView.as_view(), name='token')
]
