from django.urls import path
from . import views
from .views import *
from .views import CustomerViewSet


urlpatterns = [
   path('', index, name='base.html'),
   path('books/', view_all_books, name='all_books'),
   path('books/<int:bookid>/', view_single_book, name='single_book'),
   path('books/year/<int:year>/', books_in_year, name='books_in_year'),
   path('books/category/<str:category>/year/<int:year>/', BooksByCategoryAndYearView.as_view(), name='books_by_category_and_year'),
   path('category/<str:category>/', BooksByCategoryView.as_view(), name='books_by_category'),
   path('add', views.api_add, name='api_add'),
   path('subtract', views.api_subtract, name='api_subtract'),
   path('multiply', views.api_multiply, name='api_subtract'),
   path('divide', views.api_divide, name='api_subtract'),
   path('exponential', views.api_exponential, name='api_exponential'),
]

# urls.py

# import these statements
from django.urls import path, include
from rest_framework import routers

# create and define our router 
router = routers.DefaultRouter()
router.register(r'Customer', views.CustomerViewSet)
router.register(r'Book', views.BookViewSet)

# add the router to our urlpatterns

urlpatterns = [
# other urls
# ....
path('api/', include(router.urls)), # add the router to our urls

]