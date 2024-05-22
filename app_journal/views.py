from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django.views.generic.detail import DetailView


from app_journal.models import (
    Requirements,
    FAQ, Contacts,
    JournalMain,
    # PaperMain,
    Paper, Publication
)
from app_journal.serializers import (
    RequirementsGetSerializer,
    FAQSerializer,
    ContactsSerializer,
    JournalMainSerializer,
    # PaperMainSerializer,
    PaperSerializer,
    PublicationSerializer,
)


class RequirementsViewSet(ModelViewSet):
    queryset = Requirements.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementsGetSerializer
        return RequirementsGetSerializer


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    # permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['question']
    search_fields = ['question', 'answer']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQSerializer
        return FAQSerializer

    # def perform_create(self, serializer):
        # serializer.save(autor=self.request.user)
        # return serializer.save


class ContactsViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['first_name', 'email']
    search_fields = ['first_name', 'email', 'message']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContactsSerializer
        return ContactsSerializer

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
        return serializer.save


class JournalMainDetailViewSet(ModelViewSet):
    queryset = JournalMain.objects.all()
    serializer_class = JournalMainSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['description']
    search_fields = ['description']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return JournalMain
        return JournalMainSerializer


# class PaperMainDetailViewSet(ModelViewSet):
#     queryset = PaperMain.objects.all()
#     serializer_class = PaperMainSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['title', 'description']
#     search_fields = ['title', 'description']
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return PaperMainSerializer
#         return PaperMainSerializer


class PaperDetailViewSet(ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'author', 'keywords', 'references']
    search_fields = ['title', 'author', 'keywords', 'references']

    def get_queryset(self):
        if self.request.method == 'POST':
            return PaperMainSerializer
        return PaperMainSerializer


class PublicationDetailViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_queryset(self):
        if self.request.method == 'POST':
            return PublicationSerializer
        return PublicationSerializer
