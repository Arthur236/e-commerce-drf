from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase, APIClient

User = get_user_model()


class BaseTest(APITestCase):
    """
    Base test cases
    """
    client = APIClient()

    def setUp(self):
        self.register_url = reverse('register')
        self.merchant_register_url = reverse('merchant-register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='pass1234'
        )

        # Create a normal user
        self.user = User.objects.create(
            username='test',
            email='test@gmail.com',
        )
        self.user.set_password("password")
        self.user.save()

    def login_user(self, email, password):
        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(self.login_url, data, format='json')

        self.token = response.data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )

        self.client.login(username=email, password=password)
