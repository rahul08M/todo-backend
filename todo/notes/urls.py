# django imports
from django.urls import path

# internal imports
from .views import *


urlpatterns = [
    path('project/', test, name='v0-project-1'),
]
