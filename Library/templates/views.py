from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


def index(request):
    years_range = range(2000, 2030)
    return render(request, 'base.html', {'years_range': years_range})

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    return render(request, 'single_book.html', {'book':single_book})

def books_in_year(request, year):
    books = Book.objects.filter(year=year)
    context = {'books': books, 'year': year}
    return render(request, 'books_in_year.html', context)

class BooksByCategoryView(ListView):
    model = Book
    template_name = 'books/books_by_category.html'
    context_object_name = 'books'

    def get_queryset(self):
        category = self.kwargs['category']
        return Book.objects.filter(category=category)

class BooksByCategoryAndYearView(ListView):
    model = Book
    template_name = 'books_by_category_and_year.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        category = self.kwargs['category']
        year = self.kwargs['year']
        queryset = Book.objects.filter(category=category, year=year)
        return queryset

# views.py 
from django.http import JsonResponse # import the jsonresponse object


# assumes get parameters 
# num1 and num2
# e.g. http://127.0.0.1:8000/add?num1=5&num2=6 returns 11
def api_add(request):
	# use 1 as default
	# we should enforce type restriction by casting the value passed to a float
	# they are assumed strings by default
	# see how to cast here: https://www.w3schools.com/python/python_casting.asp
	num1 = float(request.GET.get('num1',1)) 
	num2 = float(request.GET.get('num2',1))
	added = num1 + num2 # calculate the added value
	# prepare a dict to return as a json response
  # we have to give the value 'added' a key we will call 'result'
	resp_dict = {'result':added}
	return JsonResponse(resp_dict) # return the dict as a json respone

# views.py
from django.http import JsonResponse

def api_subtract(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    subtracted = num1 - num2
    resp_dict = {'result': subtracted}
    return JsonResponse(resp_dict)

def api_multiply(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    multiplied = num1 * num2
    resp_dict = {'result': multiplied}
    return JsonResponse(resp_dict)

def api_divide(request):
    num1 = float(request.GET.get('num1', 1))
    num2 = float(request.GET.get('num2', 1))
    
    # Check if num2 is zero to avoid division by zero
    if num2 == 0:
        resp_dict = {'error': 'Cannot divide by zero'}
    else:
        divided = num1 / num2
        resp_dict = {'result': divided}
    
    return JsonResponse(resp_dict)

def api_exponential(request):
    num1 = float(request.GET.get('num1', 2))  # base
    num2 = float(request.GET.get('num2', 3))  # exponent
    result = num1 ** num2  # Calculate the exponential value
    resp_dict = {'result': result}
    return JsonResponse(resp_dict)

#views.py

## add the following imports
from rest_framework import viewsets
from .models import *
from .serializers import *

## viewset for customers
class BookViewSet(viewsets.ModelViewSet):
	serializer_class = BookSerializer
	queryset = Book.objects.all()

from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
