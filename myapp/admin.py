from django.contrib import admin
from myapp.models import *
# Register your models here.

class empadmin(admin.ModelAdmin):
    list_display = ('name','age','salary','dept')
admin.site.register(emp,empadmin)
