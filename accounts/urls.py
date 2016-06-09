from django.conf.urls import url
from . import views
from .forms import LoginForm
from django.contrib.auth.views import login, logout
from django.contrib.auth.views import password_change, password_change_done
from .forms import PassChangeForm
urlpatterns= [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', kwargs={'authentication_form': LoginForm, },
    	),
     url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={
    	'template_name':'accounts/login_form.html', 'next_page': '/'
    	}),

   #url(r'^login/$, 'login', name='login', kwargs={'template_name:'accounts/login_form.html',}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^password_change/$', password_change, kwargs={'password_change_form': PassChangeForm, 'template_name':'registration/pass_change_form.html',
    'post_change_redirect' :"/" }, name="password_change"),
    url(r'^password_change_done/$', password_change_done, {'template_name': 'registration/password_change_done.html'},   name='password_change_done'),
    url(r'^profile/update$', views.profile_update, name='profile_update'),]
