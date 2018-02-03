"""
Product api tests
"""
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework import status

from ecommerce.base_api_test import BaseTest

User = get_user_model()


class ProductTestCase(BaseTest):
    """
    Test cases for products
    """
    create_url = reverse('product-create', kwargs={'store_slug': 'test-store'})
    rud_url = reverse('product-rud', kwargs={
        'store_slug': 'test-store',
        'slug': 'test-product'
    })

    def test_create_product(self):
        """
        Test if a logged in merchant can create a product
        """
        data = {
            'name': 'Another Product',
            'description': 'Some Description'
        }
        self.login_user("merchant@gmail.com", "password")
        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_list(self):
        """
        Test that a merchant can get a list of products from a store
        """
        data = {}
        self.login_user("merchant@gmail.com", "password")
        response = self.client.get(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_product(self):
        """
        Test that a merchant can get a single product
        """
        data = {}
        self.login_user("merchant@gmail.com", "password")
        response = self.client.get(self.rud_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        """
        Test if a logged in merchant can create a product
        """
        data = {
            'name': 'Product Update',
            'description': 'Some Description'
        }
        self.login_user("merchant@gmail.com", "password")
        response = self.client.put(self.rud_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_product(self):
        """
        Test if a logged in merchant can delete a product
        """
        data = {}
        self.login_user("merchant@gmail.com", "password")
        response = self.client.delete(self.rud_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_wrong_permissions(self):
        """
        Test if a normal user can create a product
        """
        data = {
            'name': 'Another Product',
            'description': 'Some Description'
        }
        self.login_user("test@gmail.com", "password")
        response = self.client.post(self.create_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
