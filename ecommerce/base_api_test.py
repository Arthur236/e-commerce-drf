"""
Base test file
"""
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse

from rest_framework.test import APITestCase, APIClient

from stores.models import Store

User = get_user_model()


class BaseTest(APITestCase):
    """
    Base test cases
    """
    client = APIClient()
    token = ''

    def setUp(self):
        """
        Set up test data
        """
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

        # Create a merchant user
        self.merchant = User.objects.create(
            username='merchant',
            email='merchant@gmail.com',
        )
        self.merchant.set_password("password")
        self.merchant.merchant = True
        self.merchant.save()

        # Create a normal user
        self.user = User.objects.create(
            username='test',
            email='test@gmail.com',
        )
        self.user.set_password("password")
        self.user.save()

        # Create a store
        self.store = Store.objects.create(
            user=self.merchant,
            name="Test Store",
            location="Some Location"
        )

    def login_user(self, email, password):
        """
        Log in a registered user
        """
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
