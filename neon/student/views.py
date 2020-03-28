from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.models import User

from login.models import Student
# Create your views here.


@login_required(login_url='/login/')
def index(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        if user is not None:
            username = user.username
            student = Student.objects.filter(student_id = username)
            count = student.count()
            if int(count) > 0:
                c['student'] = student[0]
            return render(request,'home.html',c)
        else:
            return HttpResponseRedirect('/login/invalidlogin')
