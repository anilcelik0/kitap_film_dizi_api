from django.shortcuts import render
from book.models import books
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from . import serializers

# Create your views here.
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'count'
    max_page_size = 10000
    
class index(generics.ListAPIView):
    queryset = books.objects.all()
    serializer_class = serializers.User_Modal
    pagination_class = LargeResultsSetPagination


# http://127.0.0.1:8000/ --> http://127.0.0.1:8000/book/
def directions(request):
    return render(request,'directions.html')
