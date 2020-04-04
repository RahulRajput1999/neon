from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.models import User
from login.models import Student

@login_required(login_url='/login/')
def index(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        if user is not None:
            c['first_name'] = user.first_name
            c['last_name'] = user.last_name
            c['email'] = user.email
            return render(request,'staff_home.html',c)
        else:
            return HttpResponseRedirect('/login/invalidlogin')
# Create your views here.
