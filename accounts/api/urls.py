from django.conf.urls import url
from .views import (
    LoginView,
    LogoutView,
    MerchantRegisterAPIView,
    RegisterAPIView,
)
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    url(r'merchant-register/$', MerchantRegisterAPIView.as_view(), name='merchant-register'),
    url(r'register/$', RegisterAPIView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'^jwt/$', obtain_jwt_token),
    url(r'^jwt/refresh/$', refresh_jwt_token),
]
