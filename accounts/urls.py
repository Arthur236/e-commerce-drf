from django.conf.urls import url
from .views import RegisterAPIView

urlpatterns = [
    url(r'register/$', RegisterAPIView.as_view(), name='register'),
]
