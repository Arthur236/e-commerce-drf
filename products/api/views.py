"""
Product api views
"""
from django.db.models import Q
from rest_framework import generics, mixins

from products.models import Product
from .serializers import ProductSerializer


class ProductAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    CreateModelMixin allows us to post
    """
    lookup_field = 'slug'
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(Q(name__icontains=query) |
                           Q(description__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        """
        Add user to the serializer create method
        """
        serializer.save(user=self.request.user)

    def post(self, request, **kwargs):
        """
        Define post operations
        """
        return self.create(request, **kwargs)


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform read, update and delete operations
    """
    lookup_field = 'slug'
    serializer_class = ProductSerializer

    def get_queryset(self):
        """
        Get queryset
        """
        return Product.objects.all()
