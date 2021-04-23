from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('admin-login/', LoginView.as_view(), name="admin_login"),
    path('admin-logout/', LogoutView.as_view(), name="admin_logout"),
    path('admin-dashboard/', AdminDashboardView.as_view(), name="admin_dashboard"),

    # room
    path('admin-room-list/', RoomListView.as_view(), name='room_list'),
    path('admin-room-create/', RoomCreateView.as_view(), name='room_create'),
    path('admin-room-/<int:pk>/-update/',
         RoomUpdateView.as_view(), name='room_update'),
    path('admin-room-/<int:pk>/-delete/',
         RoomDeleteView.as_view(), name='room_delete'),
    path('admin-room-/<int:pk>/-detail/',
         RoomDetailView.as_view(), name="room_detail"),
    
    
    #news
    
    path('admin-news-list/', NewsListView.as_view(), name='news_list'),
    path('admin-news-create/', NewsCreateView.as_view(), name='news_create'),
    path('admin-news-/<int:pk>/-update/' ,NewsUpdateView.as_view(), name='news_update'),
    path('admin-news-/<int:pk>/-delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('admin-news-/<int:pk>/-detail/', NewsDetailView.as_view(), name="news_detail"),
    
]
