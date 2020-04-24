from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from neon import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('editDetails/', views.edit_details, name='editDetails'),
    path('saveDetails/', views.save_details, name='saveDetails'),
    path('examResults/', views.exam_results, name='examResults'),
    path('courseDetails/', views.course_details,name='courseDetails'),
    path('internalResult/', views.internal_result, name='internalResult'),
    path('externalResult/', views.external_result, name='externalResult'),
]
