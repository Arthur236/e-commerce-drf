"""
Store api urls
"""
from django.conf.urls import url
from .views import (
    StoreAPIView,
    StoreRUDView
)

urlpatterns = [
    url(r'(?P<slug>[\w-]+)/$', StoreRUDView.as_view(), name='store-rud'),
    url(r'$', StoreAPIView.as_view(), name='store-create'),
]
