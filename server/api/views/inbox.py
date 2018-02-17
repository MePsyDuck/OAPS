from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Inbox
from api.serializers import InboxSerializer


class InboxView(APIView):
    # No CUD
    def get(self, request, user_id):
        if request.user.id == user_id:
            inbox = Inbox.objects.filter(user_id=user_id)
            if inbox.count() != 0:
                serializer = InboxSerializer(inbox, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
