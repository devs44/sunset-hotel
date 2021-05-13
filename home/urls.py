from django.urls import path
from .import views
from .views import *

# app_name = 'home'

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
    path('gallerys/', GalleryListView.as_view(), name="gallerys"),
    path('gallerys/singleroom', SingleRoomListView.as_view(), name="single_room"),
    path('gallerys/doubleroom', DoubleRoomListView.as_view(), name="double_room"),
    path('gallerys/deluxeroom', DeluxeRoomListView.as_view(), name="deluxe_room"),
    path('gallerys/royalroom', RoyalRoomListView.as_view(), name="royal_room"),
    path('subscripton/', NewsletterView.as_view(), name="subscription"),
    # path('search/', SearchView.as_view(), name="search"),
]
