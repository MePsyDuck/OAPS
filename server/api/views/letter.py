from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import Letter
from api.serializers import LetterSerializer


class LetterView(APIView):
    def get(self, request):
        letter_id = request.data.get('id')
        try:
            letter = Letter.objects.get(pk=letter_id)
            serializer = LetterSerializer(letter)
            return Response(serializer.data)
        except Letter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            letter_id = request.data.get('id')
            letter = Letter.objects.get(id=letter_id)
            letter.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Letter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
