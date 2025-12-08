from django.contrib import admin
<<<<<<< HEAD
from myapp.models import * 
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'age', 'subject', 'class_room')
    

admin.site.register(student,studentadmin)
=======
from myapp.models import *

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','rollno','subject','marks')

# Register your models here.
admin.site.register(student,studentadmin)
>>>>>>> 5f6774e49d9cd9cf0a3fcb75114a3c24b6e24981
