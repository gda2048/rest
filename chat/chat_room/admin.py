from django.contrib import admin
from chat_room.models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin room admin"""
    list_display = ("creator", "invited_user", "date")
    filter_horizontal = ('invited', )

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])
