"""
Product api serializers
"""
from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Define product serializer
    """
    class Meta:
        """
        Specify meta data
        """
        model = Product
        fields = '__all__'

        read_only_fields = ['store', 'timestamp']
