from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('accounts.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),
]
