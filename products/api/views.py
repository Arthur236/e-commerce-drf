"""
Product api views
"""
from django.db.models import Q
from rest_framework import generics, mixins
from rest_framework.serializers import ValidationError

from ecommerce.permissions import IsMerchant, IsStoreOwner
from stores.models import Store
from products.models import Product
from .serializers import ProductSerializer


class ProductAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    CreateModelMixin allows us to post
    """
    lookup_field = 'slug'
    serializer_class = ProductSerializer
    permission_classes = (IsMerchant,)

    def get_queryset(self):
        store_slug = self.kwargs.get('store_slug')
        store = Store.objects.get(slug=store_slug)

        qs = Product.objects.filter(store=store.id)
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(Q(name__icontains=query) |
                           Q(description__icontains=query)).distinct()
        return qs

    def post(self, request, **kwargs):
        """
        Define post operations
        """
        return self.create(request, **kwargs)

    def perform_create(self, serializer):
        """
        Add store
        """
        store_slug = self.kwargs.get('store_slug')
        store = Store.objects.get(slug=store_slug)
        name = self.request.data['name']

        qs = Product.objects.filter(store=store, name__iexact=name)
        if qs.exists():
            raise ValidationError('That product already exists in that store.')

        serializer.save(store=store)


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform read, update and delete operations
    """
    lookup_field = 'slug'
    serializer_class = ProductSerializer
    permission_classes = (IsMerchant, IsStoreOwner,)

    def get_queryset(self):
        """
        Get queryset
        """
        return Product.objects.all()
