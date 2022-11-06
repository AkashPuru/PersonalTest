from django.contrib import admin
from django.urls import path
from Alert.views import home
from Alert.models import ContactForm
#from Alert.forms import ContactForm
from Alert.views import message_request
#from Alert.forms import ContactForm

admin.site.register(ContactForm)



# Register your models here.
