from django.urls import path
from app.views import *

urlpatterns = [
    path('',login_data,name='login'),
    path('reg',reg_data,name='reg')
]