from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from app_main.models import (
    Requirements,
    Category,
)


class RequirementsGetSerializer(ModelSerializer):
    requirements_title = SerializerMethodField()
    requirements_part = SerializerMethodField()
    requirements_description = SerializerMethodField()

    class Meta:
        model = Requirements
        fields = ('id', 'requirements_part', 'requirements_title', 'requirements_description')
        extra_kwargs = {
            'author': {'write_only': True}
        }

    def get_requirements_title(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_title_en
        return obj.requirements_title_uz

    def get_requirements_part(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_parts_en
        return obj.requirements_parts_uz

    def get_requirements_description(self, obj):
        lang = self.context['request'].GET.get('lang', 'uz')
        if lang == 'en':
            return obj.requirements_description_en
        return obj.requirements_description_uz


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

