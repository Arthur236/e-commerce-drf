from django.db.models import Q
from rest_framework import generics, mixins

from ecommerce.permissions import IsOwnerOrReadOnly, IsMerchant
from stores.models import Store
from .serializers import StoreSerializer


class StoreAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    """
    CreateModelMixin allows us to post
    """
    lookup_field = 'slug'
    serializer_class = StoreSerializer
    permission_classes = (IsMerchant,)

    def get_queryset(self):
        qs = Store.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(Q(name__icontains=query) |
                           Q(location__icontains=query)).distinct()
        return qs

    def perform_create(self, serializer):
        """
        Add user to the serializer create method
        """
        serializer.save(user=self.request.user)

    def post(self, request, **kwargs):
        return self.create(request, **kwargs)


class StoreRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'slug'
    serializer_class = StoreSerializer
    permission_classes = (IsOwnerOrReadOnly, IsMerchant,)

    def get_queryset(self):
        return Store.objects.all()
