from django.urls import path
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('login/', LoginView.as_view(), name="admin_login"),
    path('logout/', LogoutView.as_view(), name="admin_logout"),
    path('dashboard/', AdminDashboardView.as_view(), name="admin_dashboard"),

    # room
    path('room/list/', RoomListView.as_view(), name='room_list'),
    path('room/create/', RoomCreateView.as_view(), name='room_create'),
    path('room/<int:pk>/update/',
         RoomUpdateView.as_view(), name='room_update'),
    path('room/<int:pk>/delete/',
         RoomDeleteView.as_view(), name='room_delete'),
    path('room/<int:pk>/detail/',
         RoomDetailView.as_view(), name="room_detail"),

    # room category
    path('room/category/', RoomCategoryListView.as_view(), name='room_category'),
    path('room/category/create/',
         RoomCategoryCreateView.as_view(), name="room_cat_create"),
    path('room/category/<int:pk>/update/',
         RoomCategoryUpdateView.as_view(), name="room_cat_update"),
    path('room/category/<int:pk>/delete/',
         RoomCategoryDelete.as_view(), name='room_cat_delete'),


    # feature
    path('feature/list/', FeatureListView.as_view(), name="feature_list"),
    path('feature/create/', FeatureCreateView.as_view(), name='feature_create'),
    path('feature/<int:pk>/update/',
         FeatureUpdateView.as_view(), name='feature_update'),
    path('feature/<int:pk>/delete/',
         FeatureDeleteView.as_view(), name='feature_delete'),

    # image
    path('gallery/', ImageListView.as_view(), name='image_list'),
    path('image/create/', ImageCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image_update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),


    # news

    path('news', NewsListView.as_view(), name='news_list'),
    path('news/create', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name="news_detail"),

    # newscomment
    path('news/comment', NewsCommentTemplateView.as_view(),
         name='news_comment_list'),
    path('news/comment/create/', NewsCommentCreateView.as_view(),
         name='news_comment_create'),
    path('news/comment/<int:pk>/update/',
         NewsCommentUpdateView.as_view(), name='news_comment_update'),
    path('news/comment/<int:pk>/delete/',
         NewsCommentDeleteView.as_view(), name='news_comment_delete'),
    path('news/comment/<int:pk>/detail/',
         NewsCommentDetailView.as_view(), name="news_comment_detail"),


    # event
    path('event/list/', EventListView.as_view(), name='event_list'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('event/<int:pk>/detail/', EventDetailView.as_view(), name='event_detail'),

    # event_comments
    path('event/comment/list/', EventCommentTemplateView.as_view(),
         name='eventcomment_list'),
    path('event/commentcreate/', EventCommentCreateView.as_view(),
         name='eventcomment_create'),
    path('event/comment/<int:pk>/update/',
         EventCommentUpdateView.as_view(), name='eventcomment_update'),
    path('event/comment/<int:pk>/delete/',
         EventCommentDeleteView.as_view(), name='eventcomment_delete'),
    path('event/comment/<int:pk>/detail/',
         EventCommentDetailView.as_view(), name='eventcomment_detail'),


    # testimonials
    path('testimonial/list/', TestimonialListView.as_view(),
         name='testimonial_list'),
    path('testimonial/create/', TestimonialCreateView.as_view(),
         name='testimonial_create'),
    path('testimonial/<int:pk>/update/',
         TestimonialUpdateView.as_view(), name='testimonial_update'),
    path('testimonial/<int:pk>/delete/',
         TestimonialDeleteView.as_view(), name='testimonial_delete'),
    path('testimonial/<int:pk>/detail/',
         TestimonialDetailView.as_view(), name='testimonial_detail'),


    # message
    path('messagelist/', MessageListView.as_view(), name='message_list'),
    path('messagecreate/', MessageCreateView.as_view(), name='message_create'),
    path('message/<int:pk>/update/',
         MessageUpdateView.as_view(), name='message_update'),
    path('message/<int:pk>/delete/',
         MessageDeleteView.as_view(), name='message_delete'),
    path('message/<int:pk>/detail/',
         MessageDetailView.as_view(), name='message_detail'),

    # reservation
    path('reservationlist/', ReservationListView.as_view(),
         name='reservation_list'),
    path('reservationcreate/', ReservationCreateView.as_view(),
         name='reservation_create'),
    path('reservation/<int:pk>/update/',
         ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservation/<int:pk>/delete/',
         ReservationDeleteView.as_view(), name='reservation_delete'),
    path('reservation/<int:pk>/detail/',
         ReservationDetailView.as_view(), name='reservation_detail'),

    # servicetype
    path('service/type/list/', ServiceListView.as_view(),
         name='service_type_list'),
    path('service/type/create/', ServiceCreateView.as_view(),
         name='service_type_create'),
    path('service/type/<int:pk>/update/',
         ServiceUpdateView.as_view(), name='service_type_update'),
    path('service/type/<int:pk>/delete/',
         ServiceDeleteView.as_view(), name='service_type_delete'),
    path('service/type/<int:pk>/detail/',
         ServiceDetailView.as_view(), name='service_type_detail'),

    # servicevideo
    path('service/video/list/', ServiceVideoListView.as_view(),
         name='service_video_list'),
    path('service/video/create/', ServiceVideoCreateView.as_view(),
         name='service_video_create'),
    path('service/video/<int:pk>/update/',
         ServiceVideoUpdateView.as_view(), name='service_video_update'),
    path('service/video/<int:pk>/delete/',
         ServiceVideoDeleteView.as_view(), name='service_video_delete'),
    path('service/video/<int:pk>/detail/',
         ServiceVideoDetailView.as_view(), name='service_video_detail'),

    # contact
    path('contact/list/', ContactListView.as_view(), name='contact_list'),
    path('contact/create/', ContactCreateView.as_view(), name='contact_create'),
    path('contact/<int:pk>/update/',
         ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/',
         ContactDeleteView.as_view(), name='contact_delete'),
    path('contact/<int:pk>/detail/',
         ContactDetailView.as_view(), name='contact_detail'),

    # About
    path('about/list/', AboutView.as_view(), name="about_list"),
    path('about/create/', AboutCreateView.as_view(), name="about_create"),
    path('about/<int:pk>/update/', AboutUpdateView.as_view(), name="about_update"),
    path('about/<int:pk>/detail/', AboutDetailView.as_view(), name="about_detail"),
    path('about/<int:pk>/delete/', AboutDeleteView.as_view(), name="about_delete"),

    # room-comment

    path('room/comment/list/', RoomCommentListView.as_view(),
         name='room_comment_list'),
    path('room/commentcreate/', RoomCommentCreateView.as_view(),
         name='room_comment_create'),
    path('room/comment/<int:pk>/update/',
         RoomCommentUpdateView.as_view(), name='room_comment_update'),
    path('room/comment/<int:pk>/delete/',
         RoomCommentDeleteView.as_view(), name='room_comment_delete'),
    path('room/comment/<int:pk>/detail/',
         RoomCommentDetailView.as_view(), name='room_comment_detail'),

]
