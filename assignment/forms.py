from django import forms 
from django.forms import ModelForm 
from .models import StudentUsers,Quiz

# create a venue form 


class Answerform(ModelForm):
	class Meta:
		model  = Quiz
		fields  = ('quiz','description',)

		labels = {
		'quiz':'Question',
		'description':'',
		
		}


		widgets = {
		'quiz':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Department'}),

		'description':forms.Textarea(attrs= {'class': 'form-control', 'Placeholder':'Answer' }),

		}
		

class Addquiz(ModelForm):
	class Meta:
		model  = Quiz
		fields  = ('quiz_number','registeredStudents','date','quiz','description')

		labels = {
		'quiz_number' : '',
		'registeredStudents':'',
		'date':'DD-MM-YYYY HH:MM:SS',
		'quiz':'',
		'description':'',
		
		}


		widgets = {
		'quiz_number' : forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Course Code'}),
		'registeredStudents':forms.SelectMultiple(attrs= {'class': 'form-control', 'Placeholder': 'RegisteredStudents'}),
		'date':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder':'Date' }),
		'quiz':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Question'}),
		'description':forms.Textarea(attrs= {'class': 'form-control', 'Placeholder':'Description' }),
		# 'lecturer':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Lecturer'}),

		}
		



class Studentregister(ModelForm):
	class Meta:
		model  = StudentUsers
		fields  = ('name','department','level','address','zip_code','phone','email_address')

		labels = {
		'name' : '',
		'department':'',
		'level':'',
		'address':'',
		'zip_code':'',
		'phone':'',
		'email_address':'',
		# 'lecturer':'',
		}


		widgets = {
		'name' : forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Fullname'}),
		'department':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Password'}),
		'level':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder':'Level' }),
		'address':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Address'}),
		'zip_code':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder':'Zip-code' }),
		'phone':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder':'Phone Number' }),
		'email_address':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Email address'}),
		# 'lecturer':forms.TextInput(attrs= {'class': 'form-control', 'Placeholder': 'Lecturer'}),





		}