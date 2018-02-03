"""
Store api serializers
"""
from rest_framework import serializers

from stores.models import Store
from products.models import Product


class StoreSerializer(serializers.ModelSerializer):
    """
    Define store serializer
    """
    product_count = serializers.SerializerMethodField()

    class Meta:
        """
        Specify meta data
        """
        model = Store
        fields = (
            'name',
            'location',
            'product_count',
            'slug',
            'timestamp',
            'updated',
        )

        read_only_fields = ['user', 'slug', 'timestamp']

    def get_product_count(self, obj):
        """
        Get product count
        """
        return Product.objects.filter_by_instance(obj).count()
