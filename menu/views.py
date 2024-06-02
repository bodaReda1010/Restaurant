from django.shortcuts import render
from product.models import Product
from category.models import Category
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required(login_url='accounts:login')
def menu(request , category_slug = None):
    categories = Category.objects.all()
    if category_slug != None:
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category = category , is_active=True)
    else:
        products = Product.objects.all()
        
    context = {
        'products':products,
        'categories':categories,
    }
    return render(request , 'menu/menu.html' , context)