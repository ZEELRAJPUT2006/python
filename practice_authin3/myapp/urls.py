from django.urls import path
from myapp.views import login_data, reg_data, index_data

urlpatterns = [
    path('', login_data, name='login'),
    path('reg/', reg_data, name='reg'),
    path('index/', index_data, name='index'),
]
