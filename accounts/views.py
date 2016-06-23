from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, SignupForm2, UpdateForm, PassChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils import timezone
import datetime
from time import strftime

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
                messages.success(request, '환영합니다!')
                return redirect('accounts.views.profile')
        else:
            form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form, })
    else:
        messages.info(request, "잘못된 접근입니다.")
        return redirect('index')

@login_required
def profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.user.start.exists():
        expiration_date = get_object_or_404(User, pk=request.user.pk).start.expiration_date
        expiration_date = expiration_date.replace(tzinfo=None)
        now_time = datetime.datetime.now()
        remaining_time = expiration_date - now_time
        remaining_time = str(remaining_time.days) + "일"
        expiration_date = expiration_date.strftime("20%y.%m.%d.")
    else:
        remaining_time = "--"
        expiration_date = "--"
    return render(request, 'accounts/profile.html', {'user': user, 'remaining_time':remaining_time, 'expiration_date':expiration_date,})

@login_required
def profile_update(request):
    user = get_object_or_404(User, pk=request.user.pk)
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=user.profile)
        if form.is_valid():
            form.save()
            messages.info(request,'수정된 회원정보가 저장되었습니다!')
            return redirect('accounts.views.profile')
    else:
        form = UpdateForm(instance=user.profile)
    return render(request, 'accounts/profile_update.html', {'user':user,'form':form,})

