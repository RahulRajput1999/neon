from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/', views.programs),
    path('courses/', views.courses),
    path('exams/', views.exams),
    path('addProgram/', views.addProgram),
    path('insertProgram/', views.insertProgram),
    path('addCourse/', views.addCourse),
    path('insertCourse/', views.insertCourse),
    path('insertExam/', views.insertExam),
    path('addExam/', views.addExam),
    path('students/', views.students),
    path('addStudent/', views.addStudent),
    path('uploadStudentFile/', views.uploadStudentFile),
    path('downloadSample/', views.downloadSample),
    path('examDetails/', views.examDetails),
    path('downloadSampleResult/',views.downloadSampleResult),
    path('uploadResult/',views.uploadResult),
]
