from django.urls import path

# internal imports
from .api import *


urlpatterns = [
    path('note/', TodoAPICreateListView.as_view(), name='note-api'),
    path('note/<pk>/', TodoAPIUpdateDeleteAPIView.as_view(), name='note-api-delete'),
]