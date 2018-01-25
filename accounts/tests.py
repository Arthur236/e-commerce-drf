from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase


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
            email='test@gmail.com',
            first_name='Test',
            last_name='User'
        )
        user.set_password("password")
        user.save()

        # Define our URLs
        self.register_url = reverse('register')

    def test_register_user(self):
        """
        Test that a user is created successfully
        """
        data = {
            'email': 'user2@gmail.com',
            'first_name': 'User',
            'last_name': 'user',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 400

    def test_create_user_with_short_password(self):
        """
        Test user is not created for password lengths less than 8.
        """
        data = {
            'email': 'user3@example.com',
            'password': 'pass',
            'first_name': 'User',
            'last_name': 'user',
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_password(self):
        """
        Test user is not created without a password
        """
        data = {
            'email': 'user4@example.com',
            'password': '',
            'first_name': 'User',
            'last_name': 'user',
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_no_names(self):
        """
        Test user is not created without a first and last name
        """
        data = {
            'email': 'user5@example.com',
            'password': 'password'
        }

        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
