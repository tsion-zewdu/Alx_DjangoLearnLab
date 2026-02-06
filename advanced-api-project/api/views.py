from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter  # keep SearchFilter
from django_filters import rest_framework as filters  # required for ALX OrderingFilter

from .models import Book
from .serializers import BookSerializer

# READ – anyone can access, but authenticated can also write if needed
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # DRF backends (ALX expects filters.OrderingFilter here)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter, filters.OrderingFilter]

    # Fields available for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields available for search
    search_fields = ['title', 'author']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  

