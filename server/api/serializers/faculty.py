from rest_framework import serializers

from api.models import Faculty


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'tts_id', 'user', 'mentees')
