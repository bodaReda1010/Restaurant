from django.shortcuts import render , redirect
from . models import Account , User
from django.contrib.auth import authenticate,login,logout
from . forms import LoginForm , RegisterForm , ProfileForm , UserForm 
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request , user)
            return redirect('accounts:profile')
        else:
            return HttpResponse('Please Enter At Least All Data Without Image')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html' , {'form': form,})



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect('accounts:profile')
        else:
            return HttpResponse('Please Enter Your Username And Password')
    else:
        form = LoginForm()

    return render(request , 'accounts/login.html' , {'form': form,})



def logout_view(request):
    logout(request)
    return redirect('accounts:login')


def profile(request):
    return render(request , 'accounts/profile.html')



def edit_profile(request):
    account = Account.objects.get(user=request.user)
    if request.method == "POST":
        u = UserForm(request.POST,request.FILES,instance=request.user)
        p = ProfileForm(request.POST,request.FILES,instance=account)
        if u.is_valid() and p.is_valid():
            u.save()
            p.save()
            return redirect('accounts:profile')
    else:

        u = UserForm(instance=request.user)
        p = ProfileForm(instance=account)

    context = {
        'userForm':u,
        'profileForm' :p,
    }
    return render(request,'accounts/edit_profile.html',context)



def reset_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if confirm_password == password:
            user_exists = User.objects.filter(email = email).exists()
            if user_exists:
                user = User.objects.get(email = email)
                user.set_password(password)
                user.save()
                return redirect('accounts:profile')
        else:
            return HttpResponse('Please Enter Password Equal To Reset Password')
        
    return render(request , 'accounts/reset_password.html')