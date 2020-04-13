from django.shortcuts import render_to_response, redirect, render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from .models import *


def index(request):  # view to show the login page
    if request.user.is_authenticated:
        if request.user.is_staff:
            return HttpResponseRedirect('/staff/')
        else:
            return HttpResponseRedirect('/student')
    else:
        c = {}
        c.update(csrf(request))
        # student = Student(student_id='16CEUBG038')
        # student.save()
        return render(request, 'index.html', c)


def auth_view(request):  # view to aquthenticate the user...
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_staff:
        auth.login(request, user)
        return HttpResponseRedirect('/staff/')
    elif user is not None and not user.is_staff:
        student = Student.objects.filter(student_id=username)
        auth.login(request, user)
        return HttpResponseRedirect('/student/')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')


@login_required(login_url='/login/')
def loggedin(request):  # view for redirecting valid user to home page...
    if request.user.is_authenticated:
        return HttpResponseRedirect('/student')
    else:
        return HttpResponseRedirect('/login/invalidlogin/')


# view to redirect the invalid user to login page...
def invalidlogin(request):
    c = {}
    c.update(csrf(request))
    c['error'] = "Invalid UserName or PassWord"
    return render(request, 'index.html', c)


def logout(request):  # view for log out the user...
    auth.logout(request)
    return render(request, 'index.html')
