from django.urls import path
from rest_framework import routers
from . import views
from app_journal.views import (
    RequirementsViewSet,
    FAQViewSet,
    ContactsViewSet,
    JournalMainDetailViewSet,
    # PaperMainDetailViewSet,
    PaperDetailViewSet,
    PublicationDetailViewSet,
)

router = routers.DefaultRouter()
router.register(r'requirements', RequirementsViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'contacts', ContactsViewSet)
router.register(r'journal', JournalMainDetailViewSet)
# router.register(r'papermain', PaperMainDetailViewSet)
router.register(r'paper', PaperDetailViewSet)
router.register(r'publication', PublicationDetailViewSet)

urlpatterns = router.urls

