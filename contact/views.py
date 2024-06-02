from django.conf import settings
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from . models import Contact
from . forms import ContactForm
from django.http import HttpResponse
from accounts.models import Account
from django.contrib.auth.decorators import login_required




@login_required(login_url='accounts:login')
def contact(request):
    account = Account.objects.get(user = request.user)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact.objects.create(
                account=account,
                email=email,
                subject=subject,
                message=message,
            )
            send_mail(
                message,
                subject,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently = False,
            ) # From User To Restaurant
            return redirect('home:home')
        else:
            return HttpResponse('Please Enter Your Full Data')
    else:
        form = ContactForm()
    return render(request , 'contact/contact.html' , {'form': form,})