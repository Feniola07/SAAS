
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('assignment.urls')),
    path('students/',include('django.contrib.auth.urls')),
    path('students/',include('students.urls')),
]

# Configure Admin Titles 
admin.site.site_header  ="SAAS Admin"
admin.site.site_title  = "SAAS"
admin.site.index_title ="Home"
