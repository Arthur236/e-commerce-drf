"""
Product api urls
"""
from django.conf.urls import url
from .views import (
    ProductAPIView,
    ProductRUDView,
)

urlpatterns = [
    url(r'(?P<slug>[\w-]+)/$', ProductRUDView.as_view(), name='product-rud'),
    url(r'$', ProductAPIView.as_view(), name='product-create'),
]