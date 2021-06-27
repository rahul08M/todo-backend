from django.urls import path

# internal imports
from .api import *


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('register/', RegisterAPIView.as_view(), name='register-api')
]