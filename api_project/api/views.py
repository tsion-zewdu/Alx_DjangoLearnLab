from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import permissions

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for Book model.
    Authentication:
        - TokenAuthentication is required.
        - Only authenticated users can access.
    Usage:
        - Obtain token via /api/api-token-auth/ with username/password.
        - Include token in Authorization header for requests.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users

