from django.urls import path
from rest_framework import routers
from . import views
from app_main.views import (
    RequirementsViewSet,
    CategoryViewSet,
    CategoryListCreateView,
    CategoryDetailView,

)

router = routers.DefaultRouter()
router.register(r'requirements', RequirementsViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls


urlpatterns += [
    path('papers/<int:pk>/', CategoryListCreateView.as_view(), name='category-list'),
    path('papers/<int:pk>', CategoryDetailView.as_view(), name='category-detail')
]





