from django.core.urlresolvers import reverse

from rest_framework import status

from ecommerce.base_api_test import BaseTest


class ProfileTestCase(BaseTest):
    """
    Test cases for user profile
    """

    def test_get_profile(self):
        """
        Test that a user can get their profile
        """
        self.profile_url = reverse('profile', kwargs={
            'username': 'test'
        })
        self.login_user('test@gmail.com', 'password')

        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_superuser_get_profile(self):
        """
        Test that a superuser can get any user's profile
        """
        self.profile_url = reverse('profile', kwargs={
            'username': 'test'
        })
        self.login_user('admin@gmail.com', 'pass1234')

        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_not_logged_in(self):
        """
        Test that a user cannot get their profile when not logged in
        """
        self.profile_url = reverse('profile', kwargs={
            'username': 'test'
        })

        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_non_existent_profile(self):
        """
        Test whether a non existent profile is handled
        """
        self.profile_url = reverse('profile', kwargs={
            'username': 'non_user'
        })
        self.login_user('admin@gmail.com', 'pass1234')

        response = self.client.get(self.profile_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
