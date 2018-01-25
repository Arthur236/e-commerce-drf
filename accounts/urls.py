from django.conf.urls import url
from .views import RegisterAPIView, MerchantRegisterAPIView

urlpatterns = [
    url(r'register/$', RegisterAPIView.as_view(), name='register'),
    url(r'merchant-register/$', MerchantRegisterAPIView.as_view(), name='merchant-register'),
]
