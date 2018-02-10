from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import Letter, Inbox
from api.serializers import LetterSerializer


class LetterView(APIView):
    def get(self, request, letter_id):
        try:
            letter = Letter.objects.get(pk=letter_id)
            if Inbox.objects.filter(user=request.user, letter=letter).exists():
                serializer = LetterSerializer(letter)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Letter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = LetterSerializer(data=request.data)
        if serializer.is_valid():
            if Letter.objects.get(pk=serializer.validated_data['id']).sender == request.user:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, letter_id):
        try:
            letter = Letter.objects.get(id=letter_id)
            if letter.sender == request.user:
                letter.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except Letter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
