from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editDetails/', views.edit_details),
    path('saveDetails/', views.save_details),
]
