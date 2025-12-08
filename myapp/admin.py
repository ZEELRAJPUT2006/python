from django.contrib import admin
from myapp.models import * 
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'age', 'subject', 'class_room')
    

admin.site.register(student,studentadmin)