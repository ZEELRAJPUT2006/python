from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('display',display,name='display'),
    path('delete_data',delete_data,name='delete_data'),
    path('edit_data',edit_data,name='edit_data'),
    path('update_data',update_data,name='update_data'),
    path('search',search,name='search')
]