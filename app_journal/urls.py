from django.urls import path
from rest_framework import routers
from . import views
from app_journal.views import (
    RequirementsViewSet,
    FAQViewSet,
    ContactsViewSet,
)

router = routers.DefaultRouter()
router.register(r'requirements', RequirementsViewSet)
router.register(r'faq', FAQViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = router.urls
