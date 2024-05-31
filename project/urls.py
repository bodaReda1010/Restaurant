from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('home/',include('home.urls',namespace='home')),
    path('team/',include('team.urls',namespace='team')),
    path('about/',include('about.urls',namespace='about')),
    path('testimonials/',include('testimonials.urls',namespace='testimonials')),
    path('service/',include('service.urls',namespace='service')),
    path('menu/',include('menu.urls',namespace='menu')),
    path('booking/',include('booking.urls',namespace='booking')),
    path('contact/',include('contact.urls',namespace='contact')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
