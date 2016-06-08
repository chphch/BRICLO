from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^start_street/$', views.start_street, name='start_street'),
    url(r'^start_casual/$', views.start_casual, name='start_casual'),
    url(r'^start_both/$', views.start_both, name='start_both'),
    url(r'^faq/1/$', views.faq_detail1, name='faq_detail1'),
    url(r'^faq/2/$', views.faq_detail2, name='faq_detail2'),
    url(r'^faq/3/$', views.faq_detail3, name='faq_detail3'),
    url(r'^faq/4/$', views.faq_detail4, name='faq_detail4'),
    url(r'^faq/5/$', views.faq_detail5, name='faq_detail5'),
    url(r'^faq/6/$', views.faq_detail6, name='faq_detail6'),
    url(r'^faq/7/$', views.faq_detail7, name='faq_detail7'),
    url(r'^faq/8/$', views.faq_detail8, name='faq_detail8'),
    url(r'^faq/9/$', views.faq_detail9, name='faq_detail9'),
    url(r'^faq/10/$', views.faq_detail10, name='faq_detail10'),
    url(r'^faq/11/$', views.faq_detail11, name='faq_detail11'),
    url(r'^faq/12/$', views.faq_detail12, name='faq_detail12'),
    url(r'^faq/13/$', views.faq_detail13, name='faq_detail13'),
    url(r'^faq/14/$', views.faq_detail14, name='faq_detail14'),
]
