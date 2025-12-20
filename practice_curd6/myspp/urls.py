from django.urls import path
from myspp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('delete',delete_data,name='delete'),
    path('edit',edit_data,name='edit')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)