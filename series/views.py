from django.shortcuts import render
import json
from series.models import seriess

#API Libraries
from book.views import LargeResultsSetPagination
from rest_framework import viewsets
from . import serializers

# Filterset Librares
from django_filters import FilterSet, DateTimeFromToRangeFilter, rest_framework as filters

# Create your views here.
    
# Filterset
class seriesFilter(FilterSet):
    
    class Meta:
        model = seriess
        fields = ['creater','name','actor','type']

    
# API
class Index(viewsets.ModelViewSet):
    queryset = seriess.objects.all()
    serializer_class = serializers.User_Modal
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = seriesFilter
    pagination_class = LargeResultsSetPagination

