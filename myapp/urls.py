from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register_emp,name='register'),
    path('display',display,name='display'),
    path('delete',delete_emp,name='delete'),
    path('edit',edit_emp,name='edit'),
]