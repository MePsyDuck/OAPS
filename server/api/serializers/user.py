from rest_framework import serializers

from api.models import User


class UserSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    faculty = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_student(self, user):
        if user.is_student():
            return user.student.id
        else:
            return

    def get_faculty(self, user):
        if user.is_faculty():
            return user.faculty.id
        else:
            return
