from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms 

# to add extra fields to usercreationform create a new form to inherit the attr then add the fields
class RegisterUserForm(UserCreationForm):
	first_name = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control'}))
	last_name = forms.CharField( max_length= 100,widget = forms.TextInput(attrs= {'class': 'form-control'}))
	email=  forms.EmailField(widget = forms.EmailInput(attrs= {'class': 'form-control'}))

	class Meta:
		model  = User 
		fields  =('first_name','last_name','email','username','password1','password2')

		# to edit the default auth.forms we use below 
	def __init__(self,*args,**kwargs):
		super(RegisterUserForm,self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class']  = 'form-control'
		self.fields['password1'].widget.attrs['class']  = 'form-control'
		self.fields['password2'].widget.attrs['class']  = 'form-control'
		