from django.contrib import admin
from myapp.models import *
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display = ('name','email','image')

admin.site.register(student,studentadmin)