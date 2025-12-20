from django.contrib import admin
from myspp.models import *
# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display = ('name','price','qty','image')
admin.site.register(product,productadmin)