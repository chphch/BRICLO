from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, SignupForm2, UpdateForm, PassChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages

def signup(request):
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                authenticated_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])
                login(request, authenticated_user)
                messages.success(request, '환영합니다. ;)')
                return redirect('/')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('index')

@login_required
def profile(request):

    user = get_object_or_404(User, pk=request.user.pk)
     
    return render(request, 'accounts/profile.html', {'user': user, })


@login_required
def profile_update(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.info(request,'msg')
    else:
        form = UpdateForm(instance=user.profile)
    return render(request, 'accounts/profile_update.html', {'user':user,'form':form,})

