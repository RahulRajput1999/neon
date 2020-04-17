from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from neon import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('editDetails/', views.edit_details),
    path('saveDetails/', views.save_details),
    path('examResults/', views.exam_results),
    path('courseDetails/', views.course_details),
    path('internalResult/', views.internal_result),
    path('externalResult/', views.external_result),
]
