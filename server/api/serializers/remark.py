from rest_framework import serializers

from api.models import Remark


class RemarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remark
        fields = ('id', 'action', 'message', 'created', 'modified', 'user', 'letter')
