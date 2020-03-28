from django.shortcuts import render_to_response,redirect,render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from login.forms import *
# Create your views here.

def index(request):
    c ={}
    c.update(csrf(request))
    return render(request,'index.html',c)