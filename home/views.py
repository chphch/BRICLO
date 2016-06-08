from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import StartForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.contrib.auth.models import User


def main(request):
	return render(request, 'home/main.html', )

def faq(request):
	return render(request, 'home/index.html', )

def faq_detail1(request):
	return render(request, 'home/question1.html', )

def faq_detail2(request):
	return render(request, 'home/question2.html', )

def faq_detail3(request):
	return render(request, 'home/question3.html', )

def faq_detail4(request):
	return render(request, 'home/question4.html', )

def faq_detail5(request):
	return render(request, 'home/question5.html', )

def faq_detail6(request):
	return render(request, 'home/question6.html', )

def faq_detail7(request):
	return render(request, 'home/question7.html', )

def faq_detail8(request):
	return render(request, 'home/question8.html', )

def faq_detail9(request):
	return render(request, 'home/question9.html', )

def faq_detail10(request):
	return render(request, 'home/question10.html', )

def faq_detail11(request):
	return render(request, 'home/question11.html', )

def faq_detail12(request):
	return render(request, 'home/question12.html', )

def faq_detail13(request):
	return render(request, 'home/question13.html', )

def faq_detail14(request):
	return render(request, 'home/question14.html', )

def faq_detail15(request):
	return render(request, 'home/question15.html', )

def ordered(request):
	return render(request, 'home/ordered.html', )

@login_required(login_url='/accounts/login/')

def start_street(request):
	if request.method == "POST":
		form = StartForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.style = "street"
			post.save()
			return redirect('home.views.main')
	else:
			form = StartForm()
	return render(request, 'home/start.html', {'form': form})

def start_casual(request):
	if request.method == "POST":
		form = StartForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.style = "casual"
			post.save()
			return redirect('home.views.main')
	else:
			form = StartForm()
	return render(request, 'home/start.html', {'form': form})

def start_both(request):
	if request.method == "POST":
		form = StartForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.style = "both"
			post.save()
			return redirect('home.views.main')
	else:
			form = StartForm()
	return render(request, 'home/start.html', {'form': form})

def profile(request, user_pk):
	user = User.objects.get(pk=user_pk)
	return render(request, 'home/profile.html', {'user':user})