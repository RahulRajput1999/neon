from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editDetails/', views.edit_details),
    path('saveDetails/', views.save_details),
    path('examResults/', views.exam_results),
    path('courseDetails/', views.course_details),
    path('semcourses/',views.sem_courses),
    path('internalresult/',views.internal_result),
    path('externalresult/',views.external_result)
]
