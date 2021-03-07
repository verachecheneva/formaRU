from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from content.models import Application, Project, Tag, Questions, CompanyData
from .serializers import ApplicationSerializer, ProjectSerializer, TagSerializer, QuestionsSerializer, \
    CompanyDataSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone_number']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'slug']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.order_by('num')
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['title', 'description', 'customer', 'num']


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.order_by('num')
    serializer_class = QuestionsSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['num', 'question', 'answer']


class CompanyDataViewSet(viewsets.ModelViewSet):
    queryset = CompanyData.objects.all()
    serializer_class = CompanyDataSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['email', 'phone_number']
