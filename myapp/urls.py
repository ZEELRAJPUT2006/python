from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('edit',edit_data,name='edit'),
    path('delete',delete_data,name='delete')
]