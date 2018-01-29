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
