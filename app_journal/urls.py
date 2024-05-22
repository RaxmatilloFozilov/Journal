from django.urls import path
from rest_framework import routers
from . import views
from app_journal.views import (
    RequirementsViewSet,
    FAQViewSet,
    ContactsViewSet,
    JournalMainDetailViewSet,
    PaperMainDetailViewSet,
    # PaperDetailViewSet,
    PublicationDetailViewSet,
    PaperListCreateView, PaperDetailView
)

router = routers.DefaultRouter()
router.register(r'requirements', RequirementsViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'contacts', ContactsViewSet)
router.register(r'journal', JournalMainDetailViewSet)
router.register(r'papermain', PaperMainDetailViewSet)
router.register(r'publication', PublicationDetailViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('papers/', PaperListCreateView.as_view(), name='paper-list-create'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper-detail'),
]

