from django.contrib import admin
from .models import Room, Chat


class RoomAdmin(admin.ModelAdmin):
    list_display = ("admin", "clients", "date")

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.clients.all()])


class ChatAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "text", "date")


admin.site.register(Room, RoomAdmin)
admin.site.register(Chat, ChatAdmin)
