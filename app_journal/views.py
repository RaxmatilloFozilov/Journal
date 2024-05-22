from django.http import HttpResponseForbidden
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django.views.generic.detail import DetailView


from app_journal.models import (
    FAQ, Contacts,
    JournalMain,
    PaperMain,
    Paper, Publication,
)
from app_journal.serializers import (
    FAQSerializer,
    ContactsSerializer,
    JournalMainSerializer,
    PaperMainSerializer,
    PaperSerializer,
    PublicationSerializer,
    PublicationGetSerializer,
)


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
            return JournalMainSerializer
        return JournalMainSerializer


class PaperMainDetailViewSet(ModelViewSet):
    queryset = PaperMain.objects.all()
    serializer_class = PaperMainSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'description']
    search_fields = ['title', 'description']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PaperMainSerializer
        return PaperMainSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class PaperListCreateView(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [permissions.IsAuthenticated]  # IsAuthenticated ruxsat sinfini ishlatamiz

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("O'z maqolalaringizni ko'rish uchun login qilishingiz kerak.")
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Maqola yaratish uchun login qilishingiz kerak.")
        serializer.save(user=self.request.user)


class PaperDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return self.queryset.filter(user=self.request.user)


class PublicationDetailViewSet(ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


@api_view(['GET'])
def paper_with_parts(requiest, paper_id):
    paper_doc = PaperSerializer(Paper.objects.get(pk=paper_id))
    paper_parts = PaperSerializer(Paper.objects.filter(paper_document=paper_id), many=True)
    return Response(
         {
                'papers': paper_doc.data,
                'paper_parts': paper_parts.data,
            },
            status=status.HTTP_200_OK
)