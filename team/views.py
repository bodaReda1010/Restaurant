from django.shortcuts import render
from . models import Chef
# Create your views here.


def team(request):
    chefs = Chef.objects.all()
    context = {
        'chefs':chefs,
    }
    return render(request, 'team/team.html' , context)
