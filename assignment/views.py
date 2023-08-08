from django.shortcuts import render,redirect 
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Quiz, StudentUsers
from .forms import Studentregister,Addquiz,Answerform
from django.http import HttpResponse
import csv 

# Generate All  registered student csv 
def download_registeredstudents (request):
	response = HttpResponse(content_type ='text/csv')
	response['Content-Disposition'] ='attachement;filename =RegisteredStudents.csv'

	# Create a csv writer 
	writer  = csv.writer(response)

	# Designate models 
	students  = StudentUsers.objects.all()

	# Add columns heading to the csv file 
	writer.writerow(['NAME', 'DEPARTMENT','LEVEL','ADDRESS','PHONE','EMAIL ADDRESS'])
	# Loop through the output 
	for student in students:
		writer.writerow([student.name,student.department,student.level,student.phone,student.email_address])

	return response

# Generate  Text file Questions for Questiondownload 
def download_questions (request):
	response = HttpResponse(content_type ='text/plain')
	response['Content-Disposition'] ='attachement;filename =QuestionsandAnswers.txt'
	# lines =["This is line 1 \n",
	# "This is line 2 \n",
	# "This is line 3 \n"]

	# Designate models 
	lines  =[]
	quizs  = Quiz.objects.all()
	for quiz in quizs:
		lines.append(f'{quiz.quiz_number}\n {quiz.quiz} \n {quiz.description} \n \n \n')

	response.writelines(lines)
	return response
# Create your views here.

# to create a search button and query the database 
def search_student(request):

	if request.method == "POST":
		# sarched is the namme given to the input bar so we can target the input and know what to query the databse with 
		searched = request.POST['searched']
		students= StudentUsers.objects.filter(name__contains=searched)
		return render (request,'assignment/search_student.html',{'searched':searched , 'students': students})
	else:
		return render (request,'assignment/search_student.html',{})



def answers(request, questionsid):
	quiz = Quiz.objects.get(pk = questionsid)
	form  =Answerform(request.POST or None, instance=quiz)
	if form.is_valid():
		form.save()
		return redirect ('quiz')

	return render (request,'assignment/answer_page.html',{'quiz':quiz , 'form': form})









def add_quiz(request):
	submitted  = False 
	if request.method == "POST":
		form  = Addquiz(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/add-quiz?submitted= True')
	else:
		form  = Addquiz
		if 'submitted' in request.GET:
			submitted  = True 
	return render (request,'assignment/add_quiz.html',{'form': form , 'submitted' : submitted})



	



def studentregister(request):
	submitted  = False 
	if request.method == "POST":
		form  = Studentregister(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/studentregister?submitted= True')
	else:
		form  = Studentregister
		if 'submitted' in request.GET:
			submitted  = True 
	return render (request,'assignment/Studentregister.html',{'form': form , 'submitted' : submitted})


def quiz_page(request):
	all_quiz = Quiz.objects.all()
	return render (request,'assignment/Quiz.html',{'all_quiz' : all_quiz})

def home(request, currentuser , year  =datetime.now().year , month  =datetime.now().strftime('%B')):
	# name  = "Eniola"
	user_name = StudentUsers.objects.get(pk =currentuser)
	month  = month.title()
	# convert month to number
	month_number  = list(calendar.month_name).index(month)
	month_number = int(month_number)

	# Create a calendar 
	cal =  HTMLCalendar().formatmonth(year,month_number)

	# Get Current year 
	now =  datetime.now()
	current_year =  now.year

	# Get current time 
	time =  now. strftime('%I:%M %p')
	return render(request, 
		'assignment/home.html',{
		"user_name" : user_name,
		"year" : year,
		"month" : month,
		"month_number" : month_number,
		"cal" : cal,
		"current_year" : current_year,
		"time" : time,
		# "currentuser": currentuser
		})
