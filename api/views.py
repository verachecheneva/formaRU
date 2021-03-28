from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin


from content.models import Application, Project, Tag, Questions, CompanyData, ImageProject
from .serializers import ApplicationSerializer, ProjectReadSerializer, TagSerializer, QuestionsSerializer, \
    CompanyDataSerializer, ImageSerializer


class ModelMixinSet(ListModelMixin, RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class ApplicationMixinSet(CreateModelMixin, viewsets.GenericViewSet):
    pass


class ApplicationViewSet(ApplicationMixinSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone_number']


class TagViewSet(ModelMixinSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'slug']


class ProjectViewSet(ModelMixinSet):
    queryset = Project.objects.order_by('num')
    serializer_class = ProjectReadSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['title', 'description', 'customer', 'num']


class ImageViewSet(ModelMixinSet):
    queryset = ImageProject.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('project_id'))
        return ImageProject.objects.filter(project=project)


class QuestionsViewSet(ModelMixinSet):
    queryset = Questions.objects.order_by('num')
    serializer_class = QuestionsSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['num', 'question', 'answer']


class CompanyDataViewSet(ModelMixinSet):
    queryset = CompanyData.objects.all()
    serializer_class = CompanyDataSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['email', 'phone_number']
