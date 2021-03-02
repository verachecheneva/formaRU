from django.shortcuts import render
from rest_framework import viewsets, permissions, mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from content.models import Application, Project
from .serializers import ApplicationSerializer, ProjectSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'email', 'phone_number']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['title', 'description', 'customer']
