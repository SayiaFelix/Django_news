
# from django.urls import include, re_path
from django.contrib import admin
from django.urls import re_path as url,include


urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'', include('news.urls')),
  
]


