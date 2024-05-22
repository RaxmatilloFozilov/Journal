from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter
from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from django.views.generic.detail import DetailView


from app_main.models import (
    Requirements,
    Category,

)
from app_main.serializers import (
    RequirementsGetSerializer,
    CategorySerializer

)


class RequirementsViewSet(ModelViewSet):
    queryset = Requirements.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementsGetSerializer
        return RequirementsGetSerializer

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
        return serializer.save()


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['category', 'name']


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Category.objects.all()
        query = self.request.query_params.get('query', None)
        if query is not None:
            queryset = queryset.filter(Q(category__icontains=query) | Q(name__icontains=query))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]