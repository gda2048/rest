from rest_framework import serializers
from chat_room.models import Room, Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    "User serialization"

    class Meta:
        model = User
        fields = ('id', 'username')


class RoomSerializer(serializers.ModelSerializer):
    """Chat room serialization"""
    creator = UserSerializer()
    invited = UserSerializer(many=True)

    class Meta:
        model = Room
        fields = ("id", "creator", "invited", "date")


class MessageSerializer(serializers.ModelSerializer):
    """Char serialization"""
    user = UserSerializer()

    class Meta:
        model = Message
        fields = ('user', 'text', 'date')


class MessagePOSTSerializer(serializers.ModelSerializer):
    """Char serialization"""

    class Meta:
        model = Message
        fields = ('room', 'text', )
