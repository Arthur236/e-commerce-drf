from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

from ecommerce.base_api_test import BaseTest

User = get_user_model()


class StoreTestCase(BaseTest):
    """
    Test cases for stores
    """
    create_url = reverse('store-create')
    rud_url = reverse('store-rud', kwargs={'slug': 'test-store'})

    def test_create_store(self):
        """
        Test if a logged in user can create a store
        """
        data = {
            'name': 'Another Store',
            'location': 'Some Location'
        }
        self.login_user("merchant@gmail.com", "password")
        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_store_list(self):
        data = {}
        response = self.client.get(self.rud_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
