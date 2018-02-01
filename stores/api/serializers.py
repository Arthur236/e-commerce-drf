"""
Store api serializers
"""
from rest_framework import serializers

from stores.models import Store


class StoreSerializer(serializers.ModelSerializer):
    """
    Define store serializer
    """
    class Meta:
        """
        Specify meta data
        """
        model = Store
        fields = '__all__'

        read_only_fields = ['user', 'timestamp']
