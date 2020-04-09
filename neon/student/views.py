from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
            student = Student.objects.filter(student_id=username)
            count = student.count()
            if int(count) > 0:
                c['student'] = student[0]
                student_serializable = {}
                student_serializable['student_id'] = student[0].student_id
                student_serializable['first_name'] = student[0].first_name
                student_serializable['last_name'] = student[0].last_name
                student_serializable['session_no'] = student[0].session_no
                request.session['student'] = student_serializable
            return render(request, 'home.html', c)
        else:
            return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def exam_results(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        student = request.session['student']
        if student is not None:
            c['student'] = student
        sem_list = [1, 2, 3, 4, 5, 6, 7, 8]
        c['semesters'] = sem_list
        return render(request, 'exam_results.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


def internal_result(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        student = request.session['student']
        if student is not None:
            c['student'] = student
            sem_list = [1,2,3,4,5,6,7,8]
            c['semesters'] = sem_list
        return render(request, 'internal.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


def external_result(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        student = request.session['student']
        if student is not None:
            c['student'] = student
            sem_list = [1,2,3,4,5,6,7,8]
            c['semesters'] = sem_list
        return render(request, 'external.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url='/login/')
def course_details(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        student = request.session['student']
        if student is not None:
            c['student'] = student
            sem_list = [1,2,3,4,5,6,7,8]
            c['semesters'] = sem_list
        return render(request, 'course_details.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


def sem_courses(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        student = request.session['student']
        if student is not None:
            c['student'] = student
            sem_list = [1,2,3,4,5,6,7,8]
            c['semesters'] = sem_list
        return render(request, 'sem_courses.html',c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')

@login_required(login_url='/login/')
def edit_details(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        if user is not None:
            username = user.username
            student = Student.objects.filter(student_id=username)
            count = student.count()
            if int(count) > 0:
                c['student'] = student[0]
            return render(request, 'student_edit_details.html', c)
        else:
            return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def save_details(request):
    c = {}
    c.update(csrf(request))
    first_name = request.POST.get('first_name', '')
    middle_name = request.POST.get('middle_name', '')
    last_name = request.POST.get('last_name', '')
    gender = request.POST.get('gender', '')
    birth_date = request.POST.get('birth_date', '')
    birth_place = request.POST.get('birth_place', '')
    cast_category_code = request.POST.get('cast_category_code', '')
    sub_cast = request.POST.get('sub_cast', '')
    marital_status = request.POST.get('marital_status', '')
    mother_tongue = request.POST.get('mother_tongue', '')
    nationality = request.POST.get('nationality', '')
    blood_group = request.POST.get('blood_group', '')
    full_name = request.POST.get('full_name', '')
    occupation = request.POST.get('occupation', '')
    organization_name = request.POST.get('organization_name', '')
    annual_income = request.POST.get('annual_income', '')
    address1 = request.POST.get('address1', '')
    address2 = request.POST.get('address2', '')
    address3 = request.POST.get('address3', '')
    city = request.POST.get('city', '')
    pin_code = request.POST.get('pin_code', '')
    state = request.POST.get('state', '')
    country = request.POST.get('country', '')
    phone_no = request.POST.get('phone_no', '')
    mobile_no = request.POST.get('mobile_no', '')
    email = request.POST.get('email', '')
    local_address1 = request.POST.get('local_address1', '')
    local_address2 = request.POST.get('local_address2', '')
    local_address3 = request.POST.get('local_address3', '')
    local_city = request.POST.get('local_city', '')
    local_mobile_no = request.POST.get('local_mobile_no', '')

    if request.user.is_authenticated:
        id = request.user.id
        user = User.objects.get(id=id)
        if user is not None:
            username = user.username
            student = Student.objects.filter(student_id=username)[0]
            if student is not None:
                student.first_name = first_name
                student.middle_name = middle_name
                student.last_name = last_name
                student.gender = gender
                student.birth_date = birth_date
                student.birth_place = birth_place
                student.cast_category_code = cast_category_code
                student.sub_cast = sub_cast
                student.marital_status = marital_status
                student.mother_tongue = mother_tongue
                student.nationality = nationality
                student.blood_group = blood_group
                student.full_name = full_name
                student.occupation = occupation
                student.organization_name = organization_name
                student.annual_income = annual_income
                student.address1 = address1
                student.address2 = address2
                student.address3 = address3
                student.city = city
                student.pin_code = pin_code
                student.state = state
                student.country = country
                student.phone_no = phone_no
                student.mobile_no = mobile_no
                student.email = email
                student.local_address1 = local_address1
                student.local_address2 = local_address2
                student.local_address3 = local_address3
                student.local_city = local_city
                student.local_mobile_no = local_mobile_no
                student.save()
            return HttpResponseRedirect('/student')
        else:
            return HttpResponseRedirect('/login/invalidlogin')
