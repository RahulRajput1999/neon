from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('auth/', views.auth_view),
    path('loggedin/', views.loggedin),
    path('invalidlogin/', views.invalidlogin),
    path('logout/', views.logout),
]
