from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request):
    return render(request, "chat/room.html", {
        "room": "global",
        "room_json": "global",
        "username": request.user.username,
    })
# Create your views here.
