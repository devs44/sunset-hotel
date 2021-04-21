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

]
