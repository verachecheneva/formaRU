from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ApplicationViewSet, ProjectViewSet, TagViewSet, QuestionsViewSet, CompanyDataViewSet, ImageViewSet

router = DefaultRouter()
router.register('applications', ApplicationViewSet)
router.register('tags', TagViewSet)
router.register('projects', ProjectViewSet)
router.register('projects/(?P<project_id>[0-100]+)/images', ImageViewSet)
router.register('questions', QuestionsViewSet)
router.register('company', CompanyDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
