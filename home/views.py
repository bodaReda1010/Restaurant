from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from product.models import Product
from category.models import Category
from team.models import Chef
from testimonials.models import Comment
# Create your views here.

@login_required(login_url='accounts:login')
def home(request , category_slug=None):
    categories = Category.objects.all()
    chefs = Chef.objects.all()
    master_chef = Chef.objects.filter(job_title = 'Master Chef')
    master_chef_count = master_chef.count()
    comments = Comment.objects.all()
    if category_slug != None:
        category = Category.objects.get(slug = category_slug)
        products = Product.objects.filter(category=category , is_active=True)
    else:
        products = Product.objects.all().filter(is_active=True)

    context = {
        'products': products,
        'categories': categories,
        'chefs': chefs,
        'master_chef_count': master_chef_count,
        'comments': comments,
    }
    return render(request , 'home/home.html' , context)




