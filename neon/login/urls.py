from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='loginIndex'),
    path('auth/', views.auth_view, name='auth'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('invalidlogin/', views.invalidlogin, name='invalidlogin'),
    path('logout/', views.logout,name='logout'),
]
