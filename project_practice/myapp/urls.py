from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('delete',delete_data,name='delete'),
    path('edit',edit_name,name='edit')
]