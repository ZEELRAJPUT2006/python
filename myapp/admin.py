from django.contrib import admin
from myapp.models import *

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','rollno','subject','marks')

# Register your models here.
admin.site.register(student,studentadmin)
