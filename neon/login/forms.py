from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime

from .models import *
class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ('subject_code','name','alias','rec_status','session','credit','th_min_pass1','th_min_pass2',
				  'th_total','sess_min_pass1','sess_min_pass2','sess_total','pr_min_pass1','pr_min_pass2','pr_total',
				  'tw_min_pass1','tw_min_pass2','tw_total','total_min_pass','total_marks','syllabus')

	def clean(self):
		super(CourseForm,self).clean()
		credit=self.cleaned_data.get('credit')
		session= self.cleaned_data.get('session')

		if credit > 5:
			self._errors['credit'] = self.error_class([ 'Credit cannot be more than 5'])
		if session < 1 or session > 8:
			self.errors['session'] = self.error_class(['Session must be from 1 to 8'])

		return self.cleaned_data


class SignUpForm(UserCreationForm):
	#first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	#last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
