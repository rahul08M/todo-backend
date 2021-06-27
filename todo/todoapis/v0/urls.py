from django.urls import path, include

from .authentication import urls as auth_urls
from .todo import urls as todo_urls

urlpatterns = [
    path('auth/', include(auth_urls)),
    path('note/', include(todo_urls)),
]
