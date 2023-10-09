"""kitap_film_dizi_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from book.views import Index as book_View
from movie.views import Index as movie_View
from series.views import Index as series_View


router = DefaultRouter()
router.register(r'book', book_View)
router.register(r'movie', movie_View)
router.register(r'series', series_View)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]

from kitap_film_dizi_api import settings
from django.conf.urls.static import  static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)