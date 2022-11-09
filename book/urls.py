from django.urls import path
from book import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.directions, name='directions'),
    path('book/', views.index.as_view(),name='book'),
]