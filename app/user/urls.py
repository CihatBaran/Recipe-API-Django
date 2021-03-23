from django.urls import path
from user.api_views import CreateUserView

app_name = 'user'

urlpatterns = [
    path('new/', CreateUserView.as_view(), name="create"),
]
