# from django.conf.urls import url
from django.urls import re_path
from . import views

urlpatterns=[
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^today/$',views.news_of_day,name='newsToday')
]