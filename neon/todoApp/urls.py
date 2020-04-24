from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from neon import settings

urlpatterns = [
        path('', views.index, name='index'),
]