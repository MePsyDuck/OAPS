from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Faculty
from api.serializers import FacultySerializer


class FacultyView(APIView):
    def get(self, request, fac_id):
        try:
            fac = Faculty.objects.get(pk=fac_id)
            serializer = FacultySerializer(fac)
            return Response(serializer.data)
        except Faculty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_faculty():
                if request.user.faculty.id == serializer.validated_data['id']:
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fac_id):
        try:
            if request.user.is_faculty():
                if request.user.faculty.id == fac_id:
                    std = Faculty.objects.get(id=fac_id)
                    std.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response(status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except Faculty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
