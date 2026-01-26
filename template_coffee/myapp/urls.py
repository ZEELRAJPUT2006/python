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
    path('logout/',logout_data,name='logout'),
    path('cart',cart,name='cart'),
    path('serach',serach,name='serach'),
    path('addtocart/',addtocart,name='addtocart'),
    path('details',details,name='details'),
    path('get_product',get_product,name='get_product'),
    path('get_category',get_category,name='get_category')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)