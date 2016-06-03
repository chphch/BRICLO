from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'home.views.main', name='main'),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
   document_root=settings.MEDIA_ROOT)
