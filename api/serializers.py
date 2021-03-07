from rest_framework import serializers
from content.models import Application, Project, Tag, Questions, CompanyData


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'email', 'phone_number')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'slug', 'title', 'description', 'customer', 'main_image', 'image_1', 'image_2', 'image_3',
                  'tag', 'num')


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'num', 'question', 'answer')


class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyData
        fields = '__all__'
