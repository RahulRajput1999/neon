"""neon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
import django

urlpatterns = [
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
    path('student/', include('student.urls')),
    path('login/', include('login.urls')),
    path('staff/', include('staff.urls')),
    path('avatar/', include('avatar.urls')),
    path('todoApp/',include('todoApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

