from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required

"""
Security Measures Implemented:
1. CSRF protection enabled on all forms.
2. @permission_required ensures only users with proper permissions can access views.
3. ORM queries used to prevent SQL injection.
4. User input validated using Django forms.
"""

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  
    return render(request, 'bookshelf/book_list.html', {'books': books})


@permission_required('bookshelf.can_add_book', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():  
            form.save()
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
