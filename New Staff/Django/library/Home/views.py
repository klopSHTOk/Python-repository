from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, BookInstance

# Create your views here.
def index(request):
	bCount = Book.objects.all().count()
	iCount = BookInstance.objects.all().count()
	aCount = Author.objects.all().count()

	return render(request, 'index.html', context={'num_books': bCount, 'num_inst': iCount, 'num_authors': aCount})
