from django.urls import path
from chat_room.views import RoomAPI, MessageAPI

urlpatterns = [
    path('room/', RoomAPI.as_view()),
    path('message/', MessageAPI.as_view())
]
