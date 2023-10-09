from django.shortcuts import render
from movie.models import movies

#API Libraries
from book.views import LargeResultsSetPagination
from rest_framework import viewsets
from . import serializers

# Filterset Librares
from django_filters import FilterSet, DateTimeFromToRangeFilter, rest_framework as filters

# Create your views here.

# Filterset
class movieFilter(FilterSet):
    
    class Meta:
        model = movies
        fields = ['director','name','actor','type']

    
# API
class Index(viewsets.ModelViewSet):
    queryset = movies.objects.all()
    serializer_class = serializers.User_Modal
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = movieFilter
    pagination_class = LargeResultsSetPagination