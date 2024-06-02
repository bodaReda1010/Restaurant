from django.shortcuts import render
from . models import Chef
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='accounts:login')
def team(request):
    chefs = Chef.objects.all()
    context = {
        'chefs':chefs,
    }
    return render(request, 'team/team.html' , context)
