from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from chat_room.models import Room, Message
from chat_room.serializers import RoomSerializer, MessageSerializer, MessagePOSTSerializer


class RoomAPI(APIView):
    """Chat room api view"""

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({"data": serializer.data})


class MessageAPI(APIView):
    """Message api view"""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        messages = Message.objects.filter(room=request.GET.get("room"))
        serializer = MessageSerializer(messages, many=True)
        return Response({"data": serializer.data})

    def post(self, request):
        message = MessagePOSTSerializer(data=request.data)
        if message.is_valid():
            message.save(user=request.user)
            return Response({"status": "Add"})
        return Response({"status": "error"})

