from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import Remark
from api.serializers import RemarkSerializer


class RemarkView(APIView):
    def get(self, request):
        remark_id = request.query_params.data.get('id')
        try:
            remark = Remark.objects.get(pk=remark_id)
            serializer = RemarkSerializer(remark)
            return Response(serializer.data)
        except Remark.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = RemarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            remark_id = request.data.get('id')
            remark = Remark.objects.get(id=remark_id)
            remark.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Remark.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
