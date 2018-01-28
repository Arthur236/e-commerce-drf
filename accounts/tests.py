from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token


from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(APITestCase):
    """
    Test cases for user registration
    """
    def setUp(self):
        """
        Initialize test data
        """
        user = User.objects.create(
            username='test',
            email='test@gmail.com',
        )
        user.set_password("password")
        user.save()

        # Define our URLs
        self.register_url = reverse('register')
        self.merchant_register_url = reverse('merchant-register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')

    def test_register_user(self):
        """
        Test that a user with a valid token is created successfully
        """
        data = {
            'username': 'user',
            'email': 'user@gmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 400

        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)

    def test_create_user_with_short_password(self):
        """
        Test user is not created for password lengths less than 8.
        """
        data = {
            'username': 'user',
            'email': 'user@example.com',
            'password': 'pass'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_password(self):
        """
        Test user is not created without a password
        """
        data = {
            'username': 'user',
            'email': 'user@example.com',
            'password': ''
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_username(self):
        """
        Test user is not created without a username
        """
        data = {
            'email': 'user@example.com',
            'password': 'password'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_email(self):
        """
        Test whether a user can be registered without an email
        """
        data = {
            'username': 'user',
            'email': '',
            'password': 'password'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_preexisting_email(self):
        """
        Test whether emails are unique
        """
        data = {
            'username': 'test',
            'email': 'test@example.com',
            'password': 'password'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_merchant(self):
        """
        Test that a merchant is created successfully
        """
        data = {
            'username': 'user',
            'email': 'user@gmail.com',
            'password': 'password'
        }
        response = self.client.post(self.merchant_register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 400

        user = User.objects.latest('id')
        token = Token.objects.get(user=user)
        self.assertEqual(response.data['token'], token.key)

    def test_login_with_valid_credentials(self):
        """
        Test a user can log in with valid credentials
        """
        data = {
            'email': 'test@gmail.com',
            'password': 'password'
        }

        response = self.client.post(self.login_url, data, format('json'))
        # Assert token key exists
        self.assertIn('token', response.data)
        # Assert status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_credentials(self):
        """
        Test a user cannot log in with invalid credentials
        """
        data = {
            'email': 'test@gmail.com',
            'password': 'pass'
        }

        response = self.client.post(self.login_url, data, format('json'))
        # Assert status code is 401 UNAUTHORIZED
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
