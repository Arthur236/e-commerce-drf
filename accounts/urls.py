from django.conf.urls import url
from .views import (
    RegisterAPIView,
    MerchantRegisterAPIView,
    LoginView,
    LogoutView
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'register/$', RegisterAPIView.as_view(), name='register'),
    url(r'merchant-register/$', MerchantRegisterAPIView.as_view(), name='merchant-register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'^get-token/', obtain_auth_token),
]
