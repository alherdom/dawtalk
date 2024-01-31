from django.shortcuts import render, redirect

def home(request):
    return redirect("chat:chat_room")


def chat_room(request):
    return render(request, "chat/room.html")
