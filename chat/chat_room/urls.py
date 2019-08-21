from django.urls import path
from chat_room.views import RoomAPI

urlpatterns = [
    path('room/', RoomAPI.as_view())
]
