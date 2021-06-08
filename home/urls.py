from django.urls import path
from .import views
from .views import *

# app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('rooms/', RoomListView.as_view(), name="rooms"),
    path('room/<int:pk>/', RoomDetailView.as_view(), name="room-detail"),
    path('about/', ServiceListView.as_view(), name="about"),
    path('reservation/', ReservationView.as_view(), name="reservation"),
    path('news/', NewsListView.as_view(), name="news"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path('event/', EventListView.as_view(), name="event"),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event-detail"),
    path('contacts/', ContactTemplateView.as_view(), name="contact"),
    path('gallerys/', GalleryListView.as_view(), name="gallerys"),
    path('subscription/', SubscriptionView.as_view(), name='subscription'),
    path('unsubscribe/', UnSubscriptionView.as_view(), name='unsubscription'),
    path('seach-result/', SearchView.as_view(), name='search-result'),


]
