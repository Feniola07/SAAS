from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = "home" ),
    path('<int:year>/<str:month>',views.home,name = "home" ),
    path('quiz',views.quiz_page,name = "quiz"),
    path('studentregister',views.studentregister,name = "studentregister"),
    path('search_student',views.search_student,name = "search_student"),
    path('add-quiz',views.add_quiz,name = "add-quiz"),
    path('answers/<questionsid>',views.answers,name = "answer"),
    path('download_questions',views.download_questions,name ="download_questions" ),
    path('download_students',views.download_registeredstudents,name ="download_students"),
    path('download_questionspdf',views.download_questionspdf,name ="download_questionspdf")


]
