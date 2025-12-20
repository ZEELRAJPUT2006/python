from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('service/',service,name='service'),
    path('menu',menu,name='menu'),
    path('reservation/',reservation,name='reservation'),
    path('testimonial/',testimonial,name='testimonial'),
    path('login/',login_data,name='login'),
    path('registration/',registration,name='registration'),
    path('logout/',logout_data,name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)