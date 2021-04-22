from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', HomeListView.as_view(), name="home"),
    path('rooms/', RoomListView.as_view(), name="rooms"),
    path('room/<int:pk>/', RoomDetailView.as_view(), name="room_detail"),
    path('about/', ServiceListView.as_view(), name="about"),
    path('reservation/', ReservationView.as_view(), name="reservation"),
]


