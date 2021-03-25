from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly

from content.models import Application, Project, Tag, Questions, CompanyData, ImageProject
from .serializers import ApplicationSerializer, ProjectReadSerializer, TagSerializer, QuestionsSerializer, \
    CompanyDataSerializer, ImageSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone_number']

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'slug']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.order_by('num')
    serializer_class = ProjectReadSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['title', 'description', 'customer', 'num']
    permission_classes = [IsAuthenticatedOrReadOnly]


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageProject.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_id'))
        return ImageProject.objects.filter(project=project)


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.order_by('num')
    serializer_class = QuestionsSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['num', 'question', 'answer']
    permission_classes = [IsAuthenticatedOrReadOnly]


class CompanyDataViewSet(viewsets.ModelViewSet):
    queryset = CompanyData.objects.all()
    serializer_class = CompanyDataSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['email', 'phone_number']
    permission_classes = [IsAuthenticatedOrReadOnly]
