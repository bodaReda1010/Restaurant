from django.urls import path
from . import views

app_name = 'testimonials'

urlpatterns = [

    path('',views.testimonials,name='testimonials'),
    path('comments/',views.comments,name='comments'),
    
]