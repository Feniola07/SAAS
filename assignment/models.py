from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class StudentUsers(models.Model):
	name = models.CharField('Name', max_length= 100)
	department = models.CharField('department', max_length= 100)
	level = models.CharField('level', max_length= 100)
	address = models.CharField('address' ,max_length= 300)
	zip_code = models.CharField('Zip code ' , max_length= 10)
	phone = models.CharField('Contact Phone ', max_length= 300)
	email_address =  models.EmailField('Email',max_length= 300)
	lecturer = models.ForeignKey(User,blank =True,null =True,on_delete =models.SET_NULL)

	def __str__(self):
		return self.name







class Quiz(models.Model):
	quiz_number = models.CharField('Quiz_number', max_length= 100)
	registeredStudents = models.ManyToManyField(StudentUsers,blank = True ) 
	date = models.DateTimeField('date')
	quiz = models.CharField('quiz', max_length= 100)
	description = models.TextField(blank =True)

	def __str__(self):
		return self.quiz_number
