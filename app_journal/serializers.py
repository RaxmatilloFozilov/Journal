from rest_framework import serializers

from app_journal.models import Requirements, FAQ, Contacts


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = ['title', 'description']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'message']

