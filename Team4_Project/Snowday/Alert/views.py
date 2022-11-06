from django.shortcuts import  render, redirect
from .forms import NewUserForm
from .forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
#from .forms import ContactForm
from django.template.loader import render_to_string

def home(request):
    return HttpResponse('Website under construction')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login_request")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register/register.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect("base.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login/login.html',{"login_form": form})



def message_request(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('Contact/Email/EmailForm.html', {
                'subject':subject,
                'message':message,
                'email': email,
                })


            print('the form is valid')
            send_mail(subject,
              message,
              'DjangoMail04@gmail.com',
              [email],
              html_message = html)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'contact/index.html',{
        'form': form
        })

    
