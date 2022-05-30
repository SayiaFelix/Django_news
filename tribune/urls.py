
from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [ 
    url(r'^admin/', admin.site.urls),
    url(r'', include('news.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]


