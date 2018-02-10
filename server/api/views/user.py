from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import User
from api.serializers import UserSerializer


class UserView(APIView):
    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.id == serializer.validated_data['id']:
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        try:
            if request.user.id == user_id:
                user = User.objects.get(id=user_id)
                user.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
