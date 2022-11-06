from django.db import models
#from django.core.mail import send_mail
#from Alert.views import message_request
# Create your models here.

class ContactForm(models.Model):
	subject = models.CharField(max_length=255)
	email = models.EmailField()
	message = models.TextField(default='', blank=True)

#	message_request(1)
              