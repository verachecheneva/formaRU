from rest_framework import serializers
from content.models import Application, Project


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'email', 'phone_number')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'customer', 'main_image', 'image_1', 'image_2', 'image_3')
