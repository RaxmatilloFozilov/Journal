from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from app_journal.models import (
    Requirements, FAQ, Contacts, JournalMain,
    PaperMain, Paper,
    Publication,
)


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
        fields = ['first_name', 'email', 'message']


class JournalMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalMain
        fields = ['id', 'edition_logo', 'description']


class PaperMainSerializer(ModelSerializer):
    class Meta:
        model = PaperMain
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = ['id', 'field_name', 'title', 'author', 'year', 'number_views', 'description', 'references', 'keywords', 'file']
        read_only_fields = ['user']


class PublicationSerializer(ModelSerializer):
    publication_name = SerializerMethodField(method_name='get_publication_name', read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'


class PublicationGetSerializer(serializers.ModelSerializer):
    publication_name = SerializerMethodField(method_name='get_publication_name', read_only=True)
    publication_description = SerializerMethodField(method_name='get_publication_description', read_only=True)

    class Meta:
        model = Publication
        fields = ('id', 'publication_name', 'journal_avatar', 'publication_description', 'categories_in_journal')

    def get_publication_name(self, obj):
        try:
            lang = self.context['request'].query_params.get('lang', 'uz')
            if lang == 'en':
                return obj.jour
            return obj.publication_name_uz
        except:
            return obj.publication_name_uz

    def get_publication_description(self,obj):
        try:
            lang = self.context['request'].query_params.get('lang', 'uz')
            if lang == 'en':
                return obj.jour
            return obj.publication_description_uz
        except:
            return obj.publication_description_uz




