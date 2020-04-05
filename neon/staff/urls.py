from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('programs/',views.programs),
    path('addProgram/',views.addProgram),
    path('insertProgram/',views.insertProgram)
]