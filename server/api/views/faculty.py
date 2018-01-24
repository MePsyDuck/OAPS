from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import User, Faculty
from api.serializers import FacultySerializer


class FacultyView(APIView):
    def get(self, request):
        fac_id = request.query_params.get('id')
        try:
            fac = Faculty.objects.get(pk=fac_id)
            serializer = FacultySerializer(fac)
            return Response(serializer.data)
        except Faculty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            fac_id = request.data.get('id')
            fac = Faculty.objects.get(id=fac_id)
            fac.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
