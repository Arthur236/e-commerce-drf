from django.conf.urls import url
from .views import (
    StoreAPIView,
    StoreRUDView
)

urlpatterns = [
    url(r'$', StoreAPIView.as_view(), name='store-create'),
    url(r'(?P<slug>[\w-]+)/$', StoreRUDView.as_view(), name='store-rud'),
]
