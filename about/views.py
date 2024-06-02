from django.shortcuts import render
from team.models import Chef
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='accounts:login')
def about(request):
    chefs = Chef.objects.all()
    master_chef = Chef.objects.filter(job_title = 'Master Chef')
    master_chef_count = master_chef.count()
    context = {
        'chefs':chefs,
        'master_chef_count':master_chef_count,
    }
    return render(request, 'about/about.html' , context)