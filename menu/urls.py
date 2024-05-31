from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [

    path('',views.menu,name='menu'),
    path('<str:category_slug>/',views.menu,name='category_slug'),

]