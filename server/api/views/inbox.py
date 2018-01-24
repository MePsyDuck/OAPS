from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

from api.models import Inbox
from api.serializers import InboxSerializer


class InboxView(APIView):
    # No CUD
    def get(self, request):
        user_id = request.query_params.get('id')
        try:
            inbox = Inbox.objects.filter(user_id=user_id)
            serializer = InboxSerializer(inbox, many=True)
            return Response(serializer.data)
        except Inbox.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
