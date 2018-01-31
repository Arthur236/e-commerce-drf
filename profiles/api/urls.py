from django.conf.urls import url
from .views import (
    UserProfileRUDView
)

urlpatterns = [
    url(r'(?P<username>[\w-]+)/$', UserProfileRUDView.as_view(), name='profile'),
]
