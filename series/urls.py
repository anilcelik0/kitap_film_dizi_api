from django.urls import path
from series import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index.as_view(), name='series'),
]