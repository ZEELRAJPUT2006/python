from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(product)
admin.site.register(country)
admin.site.register(state)
admin.site.register(city)