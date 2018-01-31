from django.conf.urls import url
from .views import (
    UserProfileRUpView
)

urlpatterns = [
    url(r'(?P<username>[\w-]+)/$', UserProfileRUpView.as_view(), name='profile'),
]
