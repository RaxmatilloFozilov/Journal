from django.urls import path
from rest_framework import routers
from . import views
from app_journal.views import (
    # RequirementsViewSet,
    FAQViewSet,
    ContactsViewSet,
    JournalMainDetailViewSet,
    PaperMainDetailViewSet,
    PublicationDetailViewSet,
    PaperListCreateView, PaperDetailView,
    paper_with_parts,
)

router = routers.DefaultRouter()
router.register(r'faq', FAQViewSet)
router.register(r'contacts', ContactsViewSet)
router.register(r'journal', JournalMainDetailViewSet)
router.register(r'papermain', PaperMainDetailViewSet)
router.register(r'publication', PublicationDetailViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('papers/', PaperListCreateView.as_view(), name='paper-list-create'),
    path('papers/<int:pk>/', PaperDetailView.as_view(), name='paper-detail'),
    path('paper_parts/<int:snk_id>/', paper_with_parts, name='paper-pats')
]

