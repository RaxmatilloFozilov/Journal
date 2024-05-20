from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from app_journal.models import Requirements, FAQ, Contacts


class RequirementsGetSerializer(ModelSerializer):
    requirements_title = SerializerMethodField()
    requirements_part = SerializerMethodField()
    requirements_description = SerializerMethodField()

    class Meta:
        model = Requirements
        fields = ('id', 'requirements_part', 'requirements_title', 'requirements_description')

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


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'message']

