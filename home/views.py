from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import StartForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib import messages


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

def start(request):
	if request.user.is_authenticated() and request.user.start.exists():
		messages.info(request, "아직 브리클로 회원권 기간이 만료되지 않았습니다.")
		return redirect('home.views.main')
	else:
		if request.method == "POST":
			form = StartForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user
				post.name = request.user.profile.name
				post.style_1_1 = str(request.POST.getlist('style_1_1'))
				post.style_1_2 = str(request.POST.getlist('style_1_2'))
				post.style_1_3 = str(request.POST.getlist('style_1_3'))
				post.style_2 = str(request.POST.getlist('style_2'))
				post.style_3 = str(request.POST.getlist('style_3'))
				post.style_4 = str(request.POST.getlist('style_4'))
				post.style_5 = str(request.POST.getlist('style_5'))
				post.style_6 = str(request.POST.getlist('style_6'))
				post.style_7 = str(request.POST.getlist('style_7'))
				post.style_8 = str(request.POST.getlist('style_8'))
				post.style_9 = str(request.POST.getlist('style_9'))
				post.style_10 = str(request.POST.getlist('style_10'))
				post.style_11 = str(request.POST.getlist('style_11'))
				post.style_12 = str(request.POST.getlist('style_12'))		
				post.save()
				messages.info(request,"감사합니다! 브리클로 회원권 등록이 완료되었습니다!")
				return redirect('home.views.main')
		else:
			form = StartForm()
		return render(request, 'home/start.html', {'form': form})

def profile(request, user_pk):
	user = User.objects.get(pk=user_pk)
	return render(request, 'home/profile.html', {'user':user})