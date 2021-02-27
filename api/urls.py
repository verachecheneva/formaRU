from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import ApplicationViewSet, ProjectViewSet

router = DefaultRouter()
router.register('applications', ApplicationViewSet)
router.register('projects', ProjectViewSet)


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
