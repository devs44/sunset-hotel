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
    
    path('news', NewsListView.as_view(), name='news_list'),
    path('news/create', NewsCreateView.as_view(), name='news_create'),
    path('news-/<int:pk>/update/' ,NewsUpdateView.as_view(), name='news_update'),
    path('news-/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news-/<int:pk>/detail/', NewsDetailView.as_view(), name="news_detail"),
    
    #comment
    path('news/comment', NewsCommentListView.as_view(), name='news_comment_list'),
     path('news/comment/create/', NewsCommentCreateView.as_view(), name='news_comment_create'),
    path('news/comment/<int:pk>/update/' , NewsCommentUpdateView.as_view(), name='news_comment_update'),
    path('news/comment/<int:pk>/delete/', NewsCommentDeleteView.as_view(), name='news_comment_delete'),
    path('news/comment/<int:pk>/detail/', NewsCommentDetailView.as_view(), name="news_comment_detail"),
    

    path("room-search/", RoomSearchView.as_view(), name='roomsearch'),



   

]
