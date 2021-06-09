from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required
from . import views
app_name = 'dashboard'
urlpatterns = [

    path('login/', LoginView.as_view(), name="admin-login"),
    path('logout/', LogoutView.as_view(), name="admin-logout"),

    #     path('dashboard/', views.admindashboard, name='admin-dashboard'),
    path('updatepassword/', PasswordsChangeView.as_view(), name="update-password"),

    path('password-forgot/', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('password-reset/<int:pk>',
         PasswordResetView.as_view(), name='passwordreset'),

    path('dashboard/', AdminDashboardView.as_view(),
         name="admin-dashboard"),


    # users
    path('user/list', UsersListView.as_view(), name="user-list"),
    path('user/create', UserCreateView.as_view(), name='user-create'),

    # room
    path('room/list/', RoomListView.as_view(), name='room-list'),
    path('room/create/', RoomCreateView.as_view(), name='room-create'),
    path('room/<int:pk>/update/',
         RoomUpdateView.as_view(), name='room-update'),
    path('room/<int:pk>/detail/',
         RoomDetailView.as_view(), name="room-detail"),
    path('room/<int:pk>/delete/',
         RoomDeleteView.as_view(), name='room-delete'),

    # room image
    path('room/image/crete/', RoomImageCreateView.as_view(),
         name='room-image-create'),

    # room category
    path('room/category/', RoomCategoryListView.as_view(), name='room_category'),
    path('room/category/create/',
         RoomCategoryCreateView.as_view(), name="room-cat-create"),
    path('room/category/<int:pk>/update/',
         RoomCategoryUpdateView.as_view(), name="room-cat-update"),
    path('room/category/<int:pk>/delete/',
         RoomCategoryDelete.as_view(), name='room-cat-delete'),


    # feature
    path('feature/list/', FeatureListView.as_view(), name="feature-list"),
    path('feature/create/', FeatureCreateView.as_view(), name='feature-create'),
    path('feature/<int:pk>/update/',
         FeatureUpdateView.as_view(), name='feature-update'),
    path('feature/<int:pk>/delete/',
         FeatureDeleteView.as_view(), name='feature-delete'),

    # image
    path('gallery/', ImageListView.as_view(), name='image-list'),
    path('image/create/', ImageCreateView.as_view(), name='image-create'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image-update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image-delete'),
    #     path('image/<int:pk>/detail/', ImageDetailView.as_view(), name='image_detail'),

    # news

    path('news', NewsListView.as_view(), name='news-list'),
    path('news/create', NewsCreateView.as_view(), name='news-create'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news-update'),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name="news-detail"),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),

    # newscomment
    path('news/comment', NewsCommentTemplateView.as_view(),
         name='news-comment-list'),
    path('news/comment/create/', NewsCommentCreateView.as_view(),
         name='news-comment-create'),
    path('news/comment/<int:pk>/update/',
         NewsCommentUpdateView.as_view(), name='news-comment-update'),
    path('news/comment/<int:pk>/detail/',
         NewsCommentDetailView.as_view(), name="news-comment-detail"),
    path('news/comment/<int:pk>/delete/',
         NewsCommentDeleteView.as_view(), name='news-comment-delete'),


    # event
    path('event/list/', EventListView.as_view(), name='event-list'),
    path('event/create/', EventCreateView.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/detail/', EventDetailView.as_view(), name='event-detail'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    # event_comments
    path('event/comment/list/', EventCommentTemplateView.as_view(),
         name='event-comment-list'),
    path('event/commentcreate/', EventCommentCreateView.as_view(),
         name='event-comment-create'),
    path('event/comment/<int:pk>/update/',
         EventCommentUpdateView.as_view(), name='event-comment-update'),
    path('event/comment/<int:pk>/detail/',
         EventCommentDetailView.as_view(), name='event-comment-detail'),
    path('event/comment/<int:pk>/delete/',
         EventCommentDeleteView.as_view(), name='event-comment-delete'),


    # testimonials
    path('testimonial/list/', TestimonialListView.as_view(),
         name='testimonial-list'),
    path('testimonial/create/', TestimonialCreateView.as_view(),
         name='testimonial-create'),
    path('testimonial/<int:pk>/update/',
         TestimonialUpdateView.as_view(), name='testimonial-update'),
    path('testimonial/<int:pk>/detail/',
         TestimonialDetailView.as_view(), name='testimonial-detail'),
    path('testimonial/<int:pk>/delete/',
         TestimonialDeleteView.as_view(), name='testimonial-delete'),


    # message
    path('messagelist/', MessageListView.as_view(), name='message-list'),
    path('messagecreate/', MessageCreateView.as_view(), name='message-create'),
    path('message/<int:pk>/update/',
         MessageUpdateView.as_view(), name='message-update'),
    path('message/<int:pk>/detail/',
         MessageDetailView.as_view(), name='message-detail'),
    path('message/<int:pk>/delete/',
         MessageDeleteView.as_view(), name='message-delete'),

    # reservation
    path('reservationlist/', ReservationListView.as_view(),
         name='reservation-list'),
    path('reservationcreate/', ReservationCreateView.as_view(),
         name='reservation-create'),
    path('reservation/<int:pk>/update/',
         ReservationUpdateView.as_view(), name='reservation-update'),
    path('reservation/<int:pk>/detail/',
         ReservationDetailView.as_view(), name='reservation-detail'),
    path('reservation/<int:pk>/delete/',
         ReservationDeleteView.as_view(), name='reservation-delate'),

    # servicetype
    path('service/type/list/', ServiceListView.as_view(),
         name='service-type-list'),
    path('service/type/create/', ServiceCreateView.as_view(),
         name='service-type-create'),
    path('service/type/<int:pk>/update/',
         ServiceUpdateView.as_view(), name='service-type-update'),
    path('service/type/<int:pk>/detail/',
         ServiceDetailView.as_view(), name='service-type-detail'),
    path('service/type/<int:pk>/delete/',
         ServiceDeleteView.as_view(), name='service-type-delete'),

    # servicevideo
    path('service/video/list/', ServiceVideoListView.as_view(),
         name='service-video-list'),
    path('service/video/create/', ServiceVideoCreateView.as_view(),
         name='service-video-create'),
    path('service/video/<int:pk>/update/',
         ServiceVideoUpdateView.as_view(), name='service-video-update'),
    path('service/video/<int:pk>/detail/',
         ServiceVideoDetailView.as_view(), name='service-video-detail'),
    path('service/video/<int:pk>/delete/',
         ServiceVideoDeleteView.as_view(), name='service-video-delete'),

    # contact
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
    path('contact/create/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/',
         ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/detail/',
         ContactDetailView.as_view(), name='contact-detail'),
    path('contact/<int:pk>/delete/',
         ContactDeleteView.as_view(), name='contact-delete'),

    # About
    path('about/list/', AboutView.as_view(), name="about-list"),
    path('about/create/', AboutCreateView.as_view(), name="about-create"),
    path('about/<int:pk>/update/', AboutUpdateView.as_view(), name="about-update"),
    path('about/<int:pk>/detail/', AboutDetailView.as_view(), name="about-detail"),
    path('about/<int:pk>/delete/', AboutDeleteView.as_view(), name="about-delete"),

    # room-comment

    path('room/comment/list/', RoomCommentListView.as_view(),
         name='room-comment-list'),
    path('room/commentcreate/', RoomCommentCreateView.as_view(),
         name='room-comment-create'),
    path('room/comment/<int:pk>/update/',
         RoomCommentUpdateView.as_view(), name='room-comment-update'),
    path('room/comment/<int:pk>/detail/',
         RoomCommentDetailView.as_view(), name='room-comment-detail'),
    path('room/comment/<int:pk>/delete/',
         RoomCommentDeleteView.as_view(), name='room-comment-delete'),

    # newsletter

    path('newsletter/list/', NewsletterListView.as_view(), name='newsletter-list'),
    path('newsletter/<int:pk>/delete/',
         NewsletterDeleteView.as_view(), name='newsletter-delete'),
    # user disable
    path('userdisable/<int:pk>/',
         UserToggleStatusView.as_view(), name='user_disable'),


]
