from django.contrib import admin
from myapp.models import *

# Register your models here.

class empadmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','username','password')
admin.site.register(emp,empadmin)
