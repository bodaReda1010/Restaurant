from django.shortcuts import render , redirect
from . models import BookTable
from . forms import BookTableForm
from django.http import HttpResponse
from accounts.models import Account



def booking_table(request):
    name = Account.objects.get(user = request.user)
    if request.method == 'POST':
        form = BookTableForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            no_of_people = form.cleaned_data['no_of_people']
            date_and_time = form.cleaned_data['date_and_time']
            if int(no_of_people) > 0:
                BookTable.objects.create(
                    name = name,
                    email = email,
                    no_of_people = no_of_people,
                    date_and_time = date_and_time
                )
                return redirect('home:home')
            else:
                return HttpResponse('Number Of People Must Be More Than One')
        else:
            return HttpResponse('Please Enter Your All Data')
    else:
        form = BookTableForm()

    return render(request , 'booking/booking.html' , {'form': form,})

