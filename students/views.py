from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # Ensures only logged-in users can access the API

    def get_queryset(self):
        # Fetch only the notes belonging to the current user
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically attach the logged-in user when a new note is created
        serializer.save(user=self.request.user)