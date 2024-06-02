from django.shortcuts import render , redirect
from . models import Comment , Account
from . forms import CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='accounts:login')
def testimonials(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments
    }
    return render(request , 'testimonial/testimonial.html' , context)


@login_required(login_url='accounts:login')
def comments(request):
    account = Account.objects.get(user = request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_user = form.cleaned_data['comment']
            profession = form.cleaned_data['profession']
            Comment.objects.create(
                comment = comment_user,
                profession = profession,
                account = account
            )
            return redirect('testimonials:testimonials')
        else:
            return HttpResponse('Please Enter A Comment And Profession')
    else:
        form = CommentForm()

    return render(request , 'testimonial/comment.html' , {'form': form,})
