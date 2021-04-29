from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('rooms/', RoomListView.as_view(), name="rooms"),
    path('room/<int:pk>/', RoomDetailView.as_view(), name="room_detail"),
    path('about/', ServiceListView.as_view(), name="about"),
    path('reservation/', ReservationView.as_view(), name="reservation"),
    path('news/', NewsListView.as_view(), name="news"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news_detail"),
    path('event/', EventListView.as_view(), name="event"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
    path('contacts/', ContactTemplateView.as_view(), name="contact"),
]
