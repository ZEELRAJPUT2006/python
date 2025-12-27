from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',login_data,name='login'),
    path('reg',reg_data,name='reg'),
    path('index',index,name='index'),
    path('logout',logout_data,name='logout'),
    path('delete',delete_data,name='delete'),
    path('edit',edit_data,name='edit')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)