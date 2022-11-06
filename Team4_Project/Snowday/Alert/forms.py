from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# Create your forms here.

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=255)
	email   = forms.EmailField()
	message = forms.CharField(widget =forms.Textarea)

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	print('i am in newform')

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		print('the form in save')
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class loginForm(AuthenticationForm):
	def confirm_login_allowed(self, user):
		pass