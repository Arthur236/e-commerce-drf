from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse as api_reverse
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
            email='user1@gmail.com',
            first_name='User',
            last_name='1'
        )
        user.set_password("password")
        user.save()

    def test_created_user(self):
        """
        Test that a user can be created successfully
        """
        qs = User.objects.filter(email='user1@gmail.com')
        self.assertEqual(qs.count(), 1)

    def test_register_user_api_fail(self):
        """
        Test that registration fails with missing fields
        """
        url = api_reverse('api-auth:register')
        data = {
            'email': 'user1@gmail.com',
            'first_name': 'User',
            'last_name': '1',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # 400
        self.assertEqual(response.data['password2'][0], 'This field is required.')

    def test_register_user_api(self):
        """
        Test that a user is created successfully
        """
        url = api_reverse('api-auth:register')
        data = {
            'email': 'user1@gmail.com',
            'first_name': 'User',
            'last_name': '1',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 400
        token_len = len(response.data.get("token", 0))
        self.assertGreater(token_len, 0)

    def test_login_user_api(self):
        """
        Test that a registered user can log in
        """
        url = api_reverse('api-auth:login')
        data = {
            'email': 'user1@gmail.com',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertGreater(token_len, 0)

    def test_login_user_api_fail(self):
        """
        Test that a non registered user cannot log in
        """
        url = api_reverse('api-auth:login')
        data = {
            'email': 'user456@gmail.com',  # does not exist
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # 400
        token = response.data.get("token", 0)
        token_len = 0
        if token != 0:
            token_len = len(token)
        self.assertEqual(token_len, 0)

    def test_token_login_api(self):
        """
        Test that a user cannot log in twice within the same session
        """
        url = api_reverse('api-auth:login')
        data = {
            'email': 'user1@gmail.com',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response2 = self.client.post(url, data, format='json')
        self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

    def test_token_register_api(self):
        """
        Test that a user cannot register when they already have a token
        """
        url = api_reverse('api-auth:login')
        data = {
            'email': 'user1@gmail.com',
            'password': 'password',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # 400
        token = response.data.get("token", None)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

        url2 = api_reverse('api-auth:register')
        data2 = {
            'email': 'user2@gmail.com',
            'first_name': 'User',
            'last_name': '2',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(url2, data2, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # 403
