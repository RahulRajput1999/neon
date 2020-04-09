from djongo import models
import django.utils.timezone


# Create your models here.
class Program(models.Model):
    program_code = models.CharField(max_length=10, primary_key='true')
    institute_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    program_type = models.CharField(max_length=30)
    session_type = models.CharField(max_length=30)
    no_of_sess = models.IntegerField(default=0)
    no_of_year = models.IntegerField(default=0)
    eligibility_criteria = models.CharField(max_length=30)
    result_type = models.CharField(max_length=30)
    total_sessional = models.IntegerField(default=0)
    compulsory_sessional = models.IntegerField(default=0)


class Course(models.Model):
    subject_code = models.CharField(max_length=10, primary_key='true')
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=30)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    rec_status = models.CharField(max_length=10)
    session = models.IntegerField(default=0)
    elective = models.CharField(max_length=10)
    credit = models.IntegerField(default=0)
    th_min_pass1 = models.IntegerField(default=0)
    th_min_pass2 = models.IntegerField(default=0)
    th_total = models.IntegerField(default=0)
    sess_min_pass1 = models.IntegerField(default=0)
    sess_min_pass2 = models.IntegerField(default=0)
    sess_total = models.IntegerField(default=0)
    pr_min_pass1 = models.IntegerField(default=0)
    pr_min_pass2 = models.IntegerField(default=0)
    pr_total = models.IntegerField(default=0)
    tw_min_pass1 = models.IntegerField(default=0)
    tw_min_pass2 = models.IntegerField(default=0)
    tw_total = models.IntegerField(default=0)
    total_min_pass = models.IntegerField(default=0)
    total_marks = models.IntegerField(default=0)
    syllabus = models.CharField(max_length=50)


class Exam(models.Model):
    exam_id = models.CharField(max_length=30, primary_key='true')
    batch_year = models.CharField(max_length=10)
    attempt_type = models.CharField(max_length=10)
    session_no = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Student(models.Model):
    student_id = models.CharField(max_length=30, primary_key='true')
    admission_type = models.CharField(max_length=30, blank=True, null=True)
    ddu_reporting_date = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    name_format = models.CharField(max_length=30, default="LFM")
    gender = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    birth_place = models.CharField(max_length=30, blank=True, null=True)
    acpc_seat_allotment_date = models.DateTimeField(blank=True, null=True)
    is_d2d = models.CharField(max_length=30, blank=True, null=True)
    enrollment_year = models.CharField(max_length=30, blank=True, null=True)
    degree = models.ForeignKey(Program, on_delete=models.CASCADE)
    qualifying_exam_rollno = models.CharField(
        max_length=30, blank=True, null=True)
    session_type = models.CharField(max_length=30, blank=True, null=True)
    session_no = models.IntegerField(default=0, blank=True, null=True)
    batch_year = models.CharField(max_length=30, blank=True, null=True)
    old_student_code = models.CharField(max_length=30, blank=True, null=True)
    students_allotment = models.CharField(max_length=30, blank=True, null=True)
    merit_rank = models.IntegerField(default=0, blank=True, null=True)
    re_shuffle_status = models.CharField(max_length=30, blank=True, null=True)
    re_shuffle_phase = models.IntegerField(default=0, blank=True, null=True)
    cast_category_code = models.CharField(max_length=30, blank=True, null=True)
    sub_cast = models.CharField(max_length=30, blank=True, null=True)
    marital_status = models.CharField(max_length=30, blank=True, null=True)
    mother_tongue = models.CharField(max_length=30, blank=True, null=True)
    nationality = models.CharField(max_length=30, blank=True, null=True)
    blood_group = models.CharField(max_length=30, blank=True, null=True)
    relation_type = models.CharField(max_length=30, blank=True, null=True)
    full_name = models.CharField(max_length=30, blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    organization_name = models.CharField(max_length=30, blank=True, null=True)
    annual_income = models.IntegerField(default=0, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    address3 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    pin_code = models.CharField(max_length=30, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    phone_no = models.CharField(max_length=30, blank=True, null=True)
    mobile_no = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    local_address1 = models.CharField(max_length=30, blank=True, null=True)
    local_address2 = models.CharField(max_length=30, blank=True, null=True)
    local_address3 = models.CharField(max_length=30, blank=True, null=True)
    local_city = models.CharField(max_length=30, blank=True, null=True)
    local_mobile_no = models.CharField(max_length=30, blank=True, null=True)


class InternalResult(models.Model):
    result_id = models.CharField(max_length=30, primary_key='true')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    sess1_att = models.IntegerField(default=0)
    sess1_marks = models.IntegerField(default=0)
    lecture_Att1 = models.IntegerField(default=0)
    lecture_Att1_out_of = models.IntegerField(default=0)
    pr_Att1 = models.IntegerField(default=0)
    pr_Att1_out_of = models.IntegerField(default=0)
    sess2_att = models.IntegerField(default=0)
    sess2_marks = models.IntegerField(default=0)
    lecture_Att2 = models.IntegerField(default=0)
    lecture_Att2_out_of = models.IntegerField(default=0)
    pr_Att2 = models.IntegerField(default=0)
    pr_Att2_out_of = models.IntegerField(default=0)
    sess3_att = models.IntegerField(default=0)
    sess3_marks = models.IntegerField(default=0)
    lecture_Att3_out_of = models.IntegerField(default=0)
    lecture_Att3 = models.IntegerField(default=0)
    pr_Att3 = models.IntegerField(default=0)
    pr_Att3_out_of = models.IntegerField(default=0)
    block_att = models.IntegerField(default=0)
    block_marks = models.IntegerField(default=0)


class RegularResult(models.Model):
    result_id = models.CharField(max_length=30, primary_key='true')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    extarnal_marks = models.IntegerField(default=0)
    sessional_marks = models.IntegerField(default=0)
    practical_marks = models.IntegerField(default=0)
    termwork_marks = models.IntegerField(default=0)
    max_marks = models.IntegerField(default=0)
