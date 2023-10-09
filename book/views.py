from django.shortcuts import render
from book.models import books

#API Libraries
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from . import serializers

# Filterset Librares
from django_filters import FilterSet, DateTimeFromToRangeFilter, rest_framework as filters


# Create your views here.

#for pagination
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'count'
    max_page_size = 10000


# Filterset
class BookFilter(FilterSet):
    
    class Meta:
        model = books
        fields = ['author','name','type']

    
# API
class Index(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = serializers.User_Modal
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
    pagination_class = LargeResultsSetPagination

