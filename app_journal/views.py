from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response


from app_journal.models import (
    Requirements,
    FAQ, Contacts
)
from app_journal.serializers import (
    RequirementsSerializer,
    FAQSerializer, ContactsSerializer
)


class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RequirementsSerializer
        return RequirementsSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQSerializer
        return FAQSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactsSerializer
        return ContactsSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save
