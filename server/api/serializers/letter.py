from rest_framework import serializers

from api.models import Letter


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ('id', 'is_read', 'subject', 'body', 'created', 'modified', 'sender', 'receiver')
