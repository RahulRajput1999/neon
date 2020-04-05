from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.models import User
from login.models import Student, Program, Course, Exam
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


@login_required(login_url='/login/')
def index(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        programs = Program.objects.all()[:5]
        courses = Course.objects.all()[:5]
        exams = Exam.objects.all()[:5]
        programCount = Program.objects.all().count()
        courseCount = Course.objects.all().count()
        examCount = Exam.objects.all().count()
        studentCount = Student.objects.all().count()
        if user is not None:
            c['first_name'] = user.first_name
            c['last_name'] = user.last_name
            c['email'] = user.email
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            request.session['email'] = user.email
            c['programs'] = programs
            c['courses'] = courses
            c['studentCount'] = studentCount
            c['exams'] = exams
            c['programCount'] = programCount
            c['courseCount'] = courseCount
            c['examCount'] = examCount
            return render(request, 'staff_home.html', c)
        else:
            return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def programs(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        programsColl = Program.objects.all().order_by('name')
        page = request.GET.get('page', 1)
        paginator = Paginator(programsColl, 10)
        try:
            programs = paginator.page(page)
        except PageNotAnInteger:
            programs = paginator.page(1)
        except EmptyPage:
            programs = paginator.page(paginator.num_pages)
        c['programs'] = programs
        c['pages'] = paginator.count
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'programs.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def addProgram(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'add_program.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def insertProgram(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        program_code = request.POST.get('program_code', '')
        institute_name = request.POST.get('institute_name', '')
        name = request.POST.get('name', '')
        alias = request.POST.get('alias', '')
        program_type = request.POST.get('program_type', '')
        session_type = request.POST.get('session_type', '')
        no_of_sess = request.POST.get('no_of_sess', '')
        no_of_year = request.POST.get('no_of_year', '')
        eligibility_criteria = request.POST.get('eligibility_criteria', '')
        result_type = request.POST.get('result_type', '')
        total_sessional = request.POST.get('total_sessional', '')
        compulsory_sessional = request.POST.get('compulsory_sessional', '')
        program = Program(program_code, institute_name, name, alias, program_type, session_type, no_of_sess,
                          no_of_year, eligibility_criteria, result_type, total_sessional, compulsory_sessional)
        program.save()
        return HttpResponseRedirect('/staff/')
    else:
        return HttpResponseRedirect('/login/invalidlogin')


# Create your views here.
