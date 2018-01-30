from django.conf.urls import url
from .views import (
    UserProfileDetails
)

urlpatterns = [
    url(r'(?P<username>[\w.@+-]+)/$', UserProfileDetails.as_view(), name='profile'),
]
