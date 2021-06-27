from django.urls import path, include

from .v0 import urls as v0_urls

urlpatterns = [
    path('v0/', include(v0_urls)),
]
