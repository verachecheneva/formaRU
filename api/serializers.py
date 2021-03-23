from rest_framework import serializers
from content.models import Application, Project, Tag, Questions, CompanyData, ImageProject


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'name', 'email', 'phone_number')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectReadSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'slug_project', 'title', 'description', 'customer', 'main_image', 'tag', 'num')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageProject
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'num', 'question', 'answer')


class CompanyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyData
        fields = ('email', 'phone_number')
