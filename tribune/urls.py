from django.contrib.auth import views 
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'', include('news.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
]


