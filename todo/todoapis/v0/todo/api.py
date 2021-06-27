from django.apps.registry import apps
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import NotesSerializers


Tasks = apps.get_model('notes', 'Tasks')


class TodoAPICreateListView(generics.ListAPIView, generics.CreateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tasks.objects.all().order_by('-id')
    serializer_class = NotesSerializers

    def get_queryset(self):
        qs = self.queryset.filter(user=self.request.user)
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoAPIUpdateDeleteAPIView(generics.DestroyAPIView, generics.UpdateAPIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tasks.objects.all().order_by('-id')
    serializer_class = NotesSerializers
