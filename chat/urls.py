from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.home, name="home"),
    path("room/", views.chat_room, name="chat_room"),
]
