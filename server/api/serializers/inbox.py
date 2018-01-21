from rest_framework import serializers

from api.models import Inbox


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ('id', 'is_starred', 'user', 'letter')
