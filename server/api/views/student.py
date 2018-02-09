from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import Student
from api.serializers import StudentSerializer


class StudentView(APIView):
    def get(self, request):
        std_id = request.query_params.get('id')
        try:
            std = Student.objects.get(pk=std_id)
            serializer = StudentSerializer(std)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_student():
                if request.user.student.id == serializer.validated_data['id']:
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            std_id = request.data.get('id')
            if request.user.is_student():
                if request.user.student.id == std_id:
                    std = Student.objects.get(id=std_id)
                    std.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
