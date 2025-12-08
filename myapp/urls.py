from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register_student,name='register')
] 
