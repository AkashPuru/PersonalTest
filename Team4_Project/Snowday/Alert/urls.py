from django.urls import path
from . import views
from Alert.views import home
from Alert.views import message_request

urlpatterns = [
    path('', views.home, name='Alert'),
    path('register',views.register_request, name="register"),
    path('login',views.login_request, name="login"),
    #path('message', views.message_request, name = "message"),
     ]