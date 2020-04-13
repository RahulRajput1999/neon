from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import *
from django.contrib.auth.models import User
from login.models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from djongo.models import Count
import io
import pandas as pd
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import os


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def index(request):
    c = {}
    c.update(csrf(request))
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
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def programs(request):
    c = {}
    c.update(csrf(request))
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


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def addProgram(request):
    c = {}
    c.update(csrf(request))
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    return render(request, 'add_program.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def insertProgram(request):
    c = {}
    c.update(csrf(request))
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


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def courses(request):
    c = {}
    c.update(csrf(request))
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


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def addCourse(request):
    c = {}
    c.update(csrf(request))
    programs = Program.objects.all()
    c['programs'] = programs
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    return render(request, 'add_course.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def insertCourse(request):
    c = {}
    c.update(csrf(request))
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


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def exams(request):
    c = {}
    c.update(csrf(request))
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


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def addExam(request):
    c = {}
    c.update(csrf(request))
    courses = Course.objects.all()
    c['courses'] = courses
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    return render(request, 'add_exam.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def examDetails(request):
    c = {}
    c.update(csrf(request))
    exam_id = request.GET.get('examID', '')
    exam = Exam.objects.filter(exam_id=exam_id)
    c['exam'] = exam[0]
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    return render(request, 'exam_details.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def uploadResult(request):
    c = {}
    c.update(csrf(request))
    resultType = request.GET.get('resultType')
    exam_id = request.GET.get('examID')
    file = request.FILES['result_file']
    if resultType == 'internal':
        if file.content_type == 'text/csv':
            df = pd.read_csv(io.BytesIO(file.read()))
        elif file.content_type == 'application/vnd.ms-excel':
            df = pd.read_excel(io.BytesIO(file.read()))
        else:
            c['error'] = "File type is not supported!"
            return render(request, 'exam_details.html', c)
        receivedColumns = list(df.columns.values)
        actualColumnsInternal = ['result_id', 'student_id', 'sess1_att', 'sess1_marks', 'lecture_Att1', 'lecture_Att1_out_of', 'pr_Att1', 'pr_Att1_out_of', 'sess2_att', 'sess2_marks',
                                 'lecture_Att2', 'lecture_Att2_out_of', 'pr_Att2', 'pr_Att2_out_of', 'sess3_att', 'sess3_marks', 'lecture_Att3_out_of', 'lecture_Att3', 'pr_Att3', 'pr_Att3_out_of', 'block_att', 'block_marks']
        receivedColumns.sort()
        actualColumnsInternal.sort()
        print(df.head())
        if receivedColumns == actualColumnsInternal:
            results = []
            for index, row in df.iterrows():
                results.append(
                    InternalResult(
                        result_id=str(row['result_id']),
                        student_id=str(row['student_id']),
                        exam_id=exam_id,
                        sess1_att=str(row['sess1_att']),
                        sess1_marks=int(row['sess1_marks']),
                        lecture_Att1=int(row['lecture_Att1']),
                        lecture_Att1_out_of=row['lecture_Att1_out_of'],
                        pr_Att1=row['pr_Att1'],
                        pr_Att1_out_of=row['pr_Att1_out_of'],
                        sess2_att=row['sess2_att'],
                        sess2_marks=row['sess2_marks'],
                        lecture_Att2=row['lecture_Att2'],
                        lecture_Att2_out_of=row['lecture_Att2_out_of'],
                        pr_Att2=row['pr_Att2'],
                        pr_Att2_out_of=row['pr_Att2_out_of'],
                        sess3_att=row['sess3_att'],
                        sess3_marks=row['sess3_marks'],
                        lecture_Att3_out_of=row['lecture_Att3_out_of'],
                        lecture_Att3=row['lecture_Att3'],
                        pr_Att3=row['pr_Att3'],
                        pr_Att3_out_of=row['pr_Att3_out_of'],
                        block_att=row['block_att'],
                        block_marks=row['block_marks']
                    )
                )
            InternalResult.objects.bulk_create(results)
            return HttpResponseRedirect('/staff/exams/')
        else:
            c['error'] = "Some fields are missing or not matching in the file!"
            return render(request, 'exam_details.html', c)
    elif resultType == 'regular':
        if file.content_type == 'text/csv':
            df = pd.read_csv(io.BytesIO(file.read()))
        elif file.content_type == 'application/vnd.ms-excel':
            df = pd.read_excel(io.BytesIO(file.read()))
        else:
            c['error'] = "File type is not supported!"
            return render(request, 'exam_details.html', c)
        receivedColumns = list(df.columns.values)
        actualColumnsRegular = ['result_id', 'student_id', 'external_marks',
                                'sessional_marks', 'practical_marks', 'termwork_marks']
        receivedColumns.sort()
        actualColumnsRegular.sort()
        print(actualColumnsRegular)
        print(receivedColumns)
        if actualColumnsRegular == receivedColumns:
            results = []
            for index, row in df.iterrows():
                results.append(
                    RegularResult(
                        result_id=row['result_id'],
                        student_id=row['student_id'],
                        exam_id=exam_id,
                        external_marks=row['external_marks'],
                        sessional_marks=row['sessional_marks'],
                        practical_marks=row['practical_marks'],
                        termwork_marks=row['termwork_marks']
                    )
                )
            RegularResult.objects.bulk_create(results)
            return HttpResponseRedirect('/staff/exams/')
        else:
            c['error'] = "Some fields are missing or not matching in the file!"
            return render(request, 'exam_details.html', c)
    else:
        return HttpResponseRedirect('/staff/exams/')


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def insertExam(request):
    c = {}
    c.update(csrf(request))
    exam_id = request.POST.get('exam_id', '')
    batch_year = request.POST.get('batch_year', 0)
    attempt_type = request.POST.get('attempt_type', '')
    courseID = request.POST.get('course', '')
    date = request.POST.get('date', '')
    courseObj = Course.objects.filter(subject_code=courseID)[0]
    exam = Exam(exam_id=exam_id, batch_year=batch_year,
                attempt_type=attempt_type, session_no=courseObj.session, course=courseObj, date=date)
    exam.save()
    return HttpResponseRedirect('/staff/exams')


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
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
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def addStudent(request):
    c = {}
    c.update(csrf(request))
    courses = Course.objects.all()
    c['courses'] = courses
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    return render(request, 'add_student.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def uploadStudentFile(request):
    c = {}
    c.update(csrf(request))
    c['first_name'] = request.session['first_name']
    c['last_name'] = request.session['last_name']
    c['email'] = request.session['email']
    file = request.FILES['student_file']
    if file.content_type == 'text/csv':
        df = pd.read_csv(io.BytesIO(file.read()))
    elif file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(io.BytesIO(file.read()))
    else:
        c['error'] = "File type is not supported!"
        return render(request, 'add_student.html', c)
    receivedColumns = list(df.columns.values)
    actualColumns = ['student_id',
                     'password',
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
                     'local_mobile_no']
    receivedColumns.sort()
    actualColumns.sort()
    if receivedColumns == actualColumns:
        students = []
        users = []
        programs = Program.objects.all()
        for index, row in df.iterrows():
            user = {}
            user['username'] = str(row['student_id'])
            user['first_name'] = str(row['first_name'])
            user['last_name'] = str(row['last_name'])
            user['password1'] = str(row['password'])
            user['password2'] = str(row['password'])
            user['email'] = str(row['email'])
            form = UserCreationForm(user)
            form.save()
            program = list(
                filter(lambda x: x.program_code == row['degree'], programs))
            print(type(row['birth_date']))
            students.append(
                Student(
                    student_id=str(row['student_id']),
                    admission_type=str(row['admission_type']),
                    ddu_reporting_date=str(row['ddu_reporting_date']),
                    first_name=str(row['first_name']),
                    middle_name=str(row['middle_name']),
                    last_name=str(row['last_name']),
                    name_format=str(row['name_format']),
                    gender=str(row['gender']),
                    birth_date=str(row['birth_date']),
                    birth_place=str(row['birth_place']),
                    acpc_seat_allotment_date=str(
                        row['acpc_seat_allotment_date']),
                    is_d2d=row['is_d2d'],
                    enrollment_year=str(row['enrollment_year']),
                    degree=program[0],
                    qualifying_exam_rollno=str(
                        row['qualifying_exam_rollno']),
                    session_type=row['session_type'],
                    session_no=row['session_no'],
                    batch_year=str(row['batch_year']),
                    old_student_code=row['old_student_code'],
                    students_allotment=row['students_allotment'],
                    merit_rank=str(row['merit_rank']),
                    re_shuffle_status=row['re_shuffle_status'],
                    re_shuffle_phase=str(row['re_shuffle_phase']),
                    cast_category_code=str(row['cast_category_code']),
                    sub_cast=row['sub_cast'],
                    marital_status=row['marital_status'],
                    mother_tongue=row['mother_tongue'],
                    nationality=row['nationality'],
                    blood_group=row['blood_group'],
                    relation_type=row['relation_type'],
                    full_name=row['full_name'],
                    occupation=row['occupation'],
                    organization_name=row['organization_name'],
                    annual_income=row['annual_income'],
                    address1=row['address1'],
                    address2=row['address2'],
                    address3=['address3'],
                    city=row['city'],
                    pin_code=str(row['pin_code']),
                    state=row['state'],
                    country=row['country'],
                    phone_no=str(row['phone_no']),
                    mobile_no=str(row['mobile_no']),
                    email=row['email'],
                    local_address1=row['local_address1'],
                    local_address2=row['local_address2'],
                    local_address3=row['local_address3'],
                    local_city=row['local_city'],
                    local_mobile_no=str(row['local_mobile_no']),
                )
            )
        # User.objects.bulk_create(users)
        # students[0].save()
        Student.objects.bulk_create(students)
        return HttpResponseRedirect('/staff/students')
    else:
        print(actualColumns)
        print(receivedColumns)
        c['error'] = "Some fields are missing or not matching in the file!"
        return render(request, 'add_student.html', c)


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def downloadSample(request):
    file_name = 'students.csv'
    file_path = os.path.dirname(os.path.abspath(
        __file__)) + '/../static/assets/files/' + file_name
    excel = open(file_path, 'r')
    output = io.StringIO(excel.read())
    out_content = output.getvalue()
    output.close()
    response = HttpResponse(out_content, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.is_staff, login_url='/student/', redirect_field_name=None)
def downloadSampleResult(request):
    resultType = request.GET.get('resultType', '')
    print(resultType)
    file_name = resultType+'_result.csv'
    file_path = os.path.dirname(os.path.abspath(
        __file__)) + '/../static/assets/files/' + resultType + '_result.csv'
    excel = open(file_path, 'r')
    output = io.StringIO(excel.read())
    out_content = output.getvalue()
    output.close()
    response = HttpResponse(out_content, content_type='text/csv')
    response['Content-Disposition'] = "attachment; filename=%s" % file_name
    return response
