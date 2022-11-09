from django.shortcuts import render
from movie.models import movies
from . import serializers
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

# Create your views here.


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'count'
    max_page_size = 10000
    
class index(generics.ListAPIView):
    queryset = movies.objects.all()
    serializer_class = serializers.User_Modal
    pagination_class = LargeResultsSetPagination