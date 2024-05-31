from django.shortcuts import render
from team.models import Chef
# Create your views here.


def about(request):
    chefs = Chef.objects.all()
    master_chef = Chef.objects.filter(job_title = 'Master Chef')
    master_chef_count = master_chef.count()
    context = {
        'chefs':chefs,
        'master_chef_count':master_chef_count,
    }
    return render(request, 'about/about.html' , context)