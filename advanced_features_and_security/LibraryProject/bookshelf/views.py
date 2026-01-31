from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm
from django.shortcuts import render, redirect
from .forms import ExampleForm 
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
def form_example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})
