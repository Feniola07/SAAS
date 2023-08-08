from django.contrib import admin
from .models import StudentUsers
from .models import Quiz

# Register your models here.
# admin.site.register(StudentUsers)
admin.site.register(Quiz)

# make changes to admin page to create columns 
@admin.register(StudentUsers)
class StudentAdmin(admin.ModelAdmin):
	list_display = ('name','department','level','phone','address')
	ordering  = ('name',)
	search_fields  = ('name',)
