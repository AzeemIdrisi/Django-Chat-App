from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:room>/", views.room, name="room"),
    path("checkview", views.checkview, name="checkview"),
    path("send", views.send, name="send"),
    path("getMessages/<str:room>/", views.getMessages, name="getMessages"),
    path("delete/<str:room>/", views.delete, name="delete"),
]
