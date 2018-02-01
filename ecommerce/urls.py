"""
E-commerce base urls
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/auth/', include('accounts.api.urls')),
    url(r'^api/profiles/', include('profiles.api.urls')),
    url(r'^api/stores/', include('stores.api.urls')),
]
