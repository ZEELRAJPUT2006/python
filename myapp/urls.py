from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name='index'),
<<<<<<< HEAD
    path('register',register_student,name='register')
] 
=======
    path('edit',edit_data,name='edit'),
    path('delete',delete_data,name='delete')
]
>>>>>>> 5f6774e49d9cd9cf0a3fcb75114a3c24b6e24981
