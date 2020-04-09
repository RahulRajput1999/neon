from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.models import User
from login.models import Student, Program, Course, Exam
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from djongo.models import Count
import io
import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import static


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
        return HttpResponseRedirect('/staff/programs')
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def courses(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        courseColl = Course.objects.all().order_by('name')
        page = request.GET.get('page', 1)
        paginator = Paginator(courseColl, 10)
        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
        c['courses'] = courses
        c['pages'] = paginator.count
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'courses.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def addCourse(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        programs = Program.objects.all()
        c['programs'] = programs
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'add_course.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def insertCourse(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        subject_code = request.POST.get('subject_code', '')
        name = request.POST.get('name', '')
        alias = request.POST.get('alias', '')
        program = request.POST.get('program', '')
        rec_status = request.POST.get('rec_status', '')
        session = request.POST.get('session', 0)
        elective = request.POST.get('elective', '')
        credit = request.POST.get('credit', 0)
        th_min_pass1 = request.POST.get('th_min_pass1', 0)
        th_min_pass2 = request.POST.get('th_min_pass2', 0)
        th_total = request.POST.get('th_total', 0)
        sess_min_pass1 = request.POST.get('sess_min_pass1', 0)
        sess_min_pass2 = request.POST.get('sess_min_pass2', 0)
        sess_total = request.POST.get('sess_total', 0)
        pr_min_pass1 = request.POST.get('pr_min_pass1', 0)
        pr_min_pass2 = request.POST.get('pr_min_pass2', 0)
        pr_total = request.POST.get('pr_total', 0)
        tw_min_pass1 = request.POST.get('tw_min_pass1', 0)
        tw_min_pass2 = request.POST.get('tw_min_pass2', 0)
        tw_total = request.POST.get('tw_total', 0)
        total_min_pass = request.POST.get('total_min_pass', 0)
        total_marks = request.POST.get('total_marks', 0)
        syllabus = request.POST.get('syllabus', '--')
        programObj = Program.objects.filter(program_code=program)[0]
        course = Course(subject_code=subject_code, name=name, alias=alias, program=programObj, rec_status=rec_status, session=session, elective=elective, credit=credit, th_min_pass1=th_min_pass1, th_min_pass2=th_min_pass2, th_total=th_total, sess_min_pass1=sess_min_pass1,
                        sess_min_pass2=sess_min_pass2, sess_total=sess_total, pr_min_pass1=pr_min_pass1, pr_min_pass2=pr_min_pass2, pr_total=pr_total, tw_min_pass1=tw_min_pass1, tw_min_pass2=tw_min_pass2, tw_total=tw_total, total_min_pass=total_min_pass, total_marks=total_marks, syllabus=syllabus)
        course.save()
        return HttpResponseRedirect('/staff/courses')
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def exams(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        examColl = Exam.objects.all().order_by('exam_id')
        page = request.GET.get('page', 1)
        paginator = Paginator(examColl, 10)
        try:
            exams = paginator.page(page)
        except PageNotAnInteger:
            exams = paginator.page(1)
        except EmptyPage:
            exams = paginator.page(paginator.num_pages)
        c['exams'] = exams
        c['pages'] = paginator.count
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'exams.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def addExam(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        courses = Course.objects.all()
        c['courses'] = courses
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'add_exam.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def insertExam(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        exam_id = request.POST.get('exam_id', '')
        batch_year = request.POST.get('batch_year', 0)
        attempt_type = request.POST.get('attempt_type', '')
        session_no = request.POST.get('session_no', '')
        courseID = request.POST.get('course', '')
        date = request.POST.get('date', '')
        courseObj = Course.objects.filter(subject_code=courseID)[0]
        exam = Exam(exam_id=exam_id, batch_year=batch_year,
                    attempt_type=attempt_type, session_no=session_no, course=courseObj, date=date)
        exam.save()
        return HttpResponseRedirect('/staff/exams')
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def students(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        studentCount = Student.objects.values(
            'degree').annotate(dcount=Count('degree'))
        c['data'] = studentCount
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'students.html', c)
    else:
        return HttpResponseRedirect('/logoin/invalidlogin')


@login_required(login_url='/login/')
def addStudent(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        courses = Course.objects.all()
        c['courses'] = courses
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        return render(request, 'add_student.html', c)
    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def uploadStudentFile(request):
    c = {}
    c.update(csrf(request))
    if request.user.is_authenticated:
        c['first_name'] = request.session['first_name']
        c['last_name'] = request.session['last_name']
        c['email'] = request.session['email']
        file = request.FILES['student_file']
        if file.content_type == 'text/csv':
            df = pd.read_csv(io.BytesIO(file.read()))
            # print(df.head())
        elif file.content_type == 'application/vnd.ms-excel':
            df = pd.read_excel(io.BytesIO(file.read()))
            # print(list(df.columns.values))
        else:
            c['error'] = "File type is not supported!"
            return render(request, 'add_student.html', c)
        receivedColumns = list(df.columns.values)
        actualColumns = ['student_id',
                         'admission_type',
                         'ddu_reporting_date',
                         'first_name',
                         'middle_name',
                         'last_name',
                         'name_format',
                         'gender',
                         'birth_date',
                         'birth_place',
                         'acpc_seat_allotment_date',
                         'is_d2d',
                         'enrollment_year',
                         'degree',
                         'qualifying_exam_rollno',
                         'session_type',
                         'session_no',
                         'batch_year',
                         'old_student_code',
                         'students_allotment',
                         'merit_rank',
                         're_shuffle_status',
                         're_shuffle_phase',
                         'cast_category_code',
                         'sub_cast',
                         'marital_status',
                         'mother_tongue',
                         'nationality',
                         'blood_group',
                         'relation_type',
                         'full_name',
                         'occupation',
                         'organization_name',
                         'annual_income',
                         'address1',
                         'address2',
                         'address3',
                         'city',
                         'pin_code',
                         'state',
                         'country',
                         'phone_no',
                         'mobile_no',
                         'email',
                         'local_address1',
                         'local_address2',
                         'local_address3',
                         'local_city',
                         'local_mobile_no',
                         'courses']
        receivedColumns.sort()
        actualColumns.sort()
        if receivedColumns == actualColumns:
            return HttpResponseRedirect('/staff/students')
        else:
            c['error'] = "Some fields are missing or not matching in the file!"
            return render(request, 'add_student.html', c)

    else:
        return HttpResponseRedirect('/login/invalidlogin')


@login_required(login_url='/login/')
def downloadSample(request):
    file_path = '/home/rahul/projects/django/neon/neon/static/assets/files/students.csv'
    file_name = 'students.csv'
    excel = open(file_path, 'r')
    # mime_type = 'application/vnd.ms-excel'
    # response = HttpResponse(fl, content_type=mime_type)
    # response['Content-Disposition'] = "attachment; filename=%s" % file_name
    # response['']
    output = io.StringIO(excel.read())
    out_content = output.getvalue()
    output.close()
    response = HttpResponse(out_content, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    # return response
    return response
