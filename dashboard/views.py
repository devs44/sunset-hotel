from .mixin import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.db.models import Q
# from django.contrib import messages

from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, View, ListView, CreateView, UpdateView, DeleteView


from .models import Room, News, Comment, RoomImage, Event, Room_Category, Feature, Image, Testomonial, Message, Reservation, Services_type, Services_description, Contact,  About
from django.shortcuts import render, redirect


# Create your views here.


class LoginView(FormView):
    template_name = 'dashboard/auth/login.html'
    form_class = StaffLoginForm
    success_url = reverse_lazy('dashboard:admin_dashboard')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        pword = form.cleaned_data['password']
        user = authenticate(username=username, password=pword)

        if user is not None:
            login(self.request, user)

        else:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid Username or password',
                              'form': form
                          })

        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AdminDashboardView(DashboardMixin, TemplateView):
    template_name = 'dashboard/base/admindashboard.html'


# rooms
class RoomListView(DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/room/roomlist.html'
    model = Room
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if "room_no" in self.request.GET:
            if self.request.GET.get('room_no') != '':
                queryset = queryset.filter(
                    room_no=self.request.GET.get("room_no"))
        if "room_type" in self.request.GET:
            if self.request.GET.get('room_type') != '':
                queryset = queryset.filter(
                    room_type__title__contains=self.request.GET.get(
                        "room_type")
                )
        if "price" in self.request.GET:
            if self.request.GET.get('price') != '':
                queryset = queryset.filter(
                    price=self.request.GET.get("price")
                )

        return queryset


class RoomCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/room/roomcreate.html'
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


class RoomUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/room/roomcreate.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


class RoomDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/room/roomdetail.html'
    model = Room
    context_object_name = 'roomdetail'


class RoomDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Room
    success_url = reverse_lazy('dashboard:room_list')


class RoomCategoryListView(QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/room_category/roomcategory.html'
    model = Room_Category
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if "room_category" in self.request.GET:
            if self.request.GET.get('room_category') != '':
                queryset = queryset.filter(
                    title__contains=self.request.GET.get("room_category"))

        return queryset


class RoomCategoryCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')


class RoomCategoryUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    model = Room_Category
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')

# Feature


class FeatureListView(DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/feature/feature.html'
    model = Feature
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'room_feature' in self.request.GET:
            if self.request.GET.get('room_feature') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('room_feature')
                )
        return queryset


class FeatureCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/feature/featurecreate.html'
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/feature/featurecreate.html'
    model = Feature
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureDeleteView(DashboardMixin, DeleteMixin, DeleteView):
    model = Feature
    success_url = reverse_lazy('dashboard:feature_list')


class RoomCategoryDelete(DeleteMixin, DashboardMixin, DeleteView):
    template_name = 'dashboard/room_category/roomcategorydelete.html'
    model = Room_Category
    success_url = reverse_lazy('dashboard:room_category')


# Image
class ImageListView(QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/gallery/imagelist.html'
    model = Image


class ImageCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('dashboard:image_list')

# event


class EventListView(DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/event/eventlist.html'
    model = Event
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get("title"))
        return queryset


class EventCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/event/eventcreate.html'
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/event/eventcreate.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/event/eventdetail.html'
    model = Event
    context_object_name = 'eventdetail'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class EventDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('dashboard:event_list')

# event comment


class EventCommentTemplateView(QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/event_comment/eventcommentlist.html'
    model = Comment
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(room__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "full_name" in self.request.GET:
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name=self.request.GET.get("full_name"))
        return queryset


class EventCommentCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    model = Comment
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/event_comment/eventcommentdetail.html'
    model = Comment
    context_object_name = 'eventdetail'


class EventCommentDeleteView(DeleteMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:eventcomment_list')


class RoomSearchView(View):
    def get(self, request, *args, **kwargs):
        room = request.GET.get('room_search')
        queryset = Room.objects.all()
        if room:
            queryset = queryset.filter(room_type__icontains=room)
        return queryset


# news
class NewsListView(QuerysetMixin, DashboardMixin, ListView):
    model = News
    template_name = 'dashboard/news/list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'title' in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('title')
                )
        return queryset


class NewsCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/news/form.html'
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/news/form.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/news/detail.html'
    model = News
    context_object_name = 'newsdetail'


class NewsDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = News
    success_url = reverse_lazy('dashboard:news_list')


# newscomments

class NewsCommentTemplateView(QuerysetMixin, DashboardMixin, ListView):
    model = Comment
    template_name = 'dashboard/news_comment/list.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(events__isnull=True),
                                                 Q(room__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if 'full_name' in self.request.GET:
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name__icontains=self.request.GET.get('full_name')
                )
        return queryset


class NewsCommentCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/news_comment/form.html'
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/news_comment/form.html'
    model = Comment
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentDetailView(DetailView):
    template_name = 'dashboard/news_comment/detail.html'
    model = Comment
    context_object_name = 'commentdetail'


class NewsCommentDeleteView(DeleteMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:news_comment_list')


# testimonial
class TestimonialListView(QuerysetMixin, ListView):
    model = Testomonial
    template_name = 'dashboard/testimonial/list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if "name" in self.request.GET:
            if self.request.GET.get('name') != '':
                queryset = queryset.filter(
                    name__icontains=self.request.GET.get('name')
                )
        if "profession" in self.request.GET:
            queryset = queryset.filter(
                profession__icontains=self.request.GET.get("profession")
            )

        return queryset


class TestimonialCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/testimonial/form.html'
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/testimonial/form.html'
    model = Testomonial
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/testimonial/detail.html'
    model = Testomonial
    context_object_name = 'testimonialdetail'


class TestimonialDeleteView(DashboardMixin, DeleteMixin, DeleteView):
    model = Testomonial
    success_url = reverse_lazy('dashboard:testimonial_list')

# message


class MessageListView(QuerysetMixin, DashboardMixin, ListView):
    model = Message
    template_name = 'dashboard/message/list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        if "email" in self.request.GET:
            queryset = queryset.filter(
                email=self.request.GET.get("email")
            )

        return queryset


class MessageCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/message/form.html'
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


class MessageUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/message/form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


class MessageDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/message/detail.html'
    model = Message
    context_object_name = 'messagedetail'


class MessageDeleteView(DeleteMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('dashboard:message_list')

# reservation


class ReservationListView(QuerysetMixin, DashboardMixin, ListView):
    model = Reservation
    template_name = 'dashboard/reservation/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "first_name" in self.request.GET:
            if self.request.GET.get('first_name') != '':
                queryset = queryset.filter(
                    first_name=self.request.GET.get("first_name"))
        if "selected_room" in self.request.GET:
            if self.request.GET.get('selected_room') != '':
                queryset = queryset.filter(
                    selected_room=self.request.GET.get(
                        "selected_room")
                )
        if "check_in_date" in self.request.GET:
            if self.request.GET.get('check_in_date') != '':
                queryset = queryset.filter(
                    check_in_date=self.request.GET.get("check_in_date")
                )

        return queryset


class ReservationCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/reservation/form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


class ReservationUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/reservation/form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


class ReservationDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/reservation/detail.html'
    model = Reservation
    context_object_name = 'reservationdetail'


class ReservationDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Reservation
    success_url = reverse_lazy('dashboard:reservation_list')


class AboutView(QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/about/about.html'
    model = About
    paginate_by = 7

# About


class AboutCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:about_list')


class AboutUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    model = About
    success_url = reverse_lazy('dashboard:about_list')


class AboutDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/about/aboutdetail.html'
    model = About
    context_object_name = 'aboutdetail'


class AboutDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = About
    success_url = reverse_lazy('dashboard:about_list')


# Service Type

class ServiceListView (QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/services-type/list.html'
    model = Services_type

    def get_queryset(self):
        queryset = super().get_queryset()
        if "service_type_name" in self.request.GET:
            if self.request.GET.get('service_type_name') != '':
                queryset = queryset.filter(
                    service_type_name__contains=self.request.GET.get(
                        "service_type_name")
                )

        return queryset


class ServiceCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/services-type/form.html'
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/services-type/form.html'
    model = Services_type
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/services-type/detail.html'
    model = Services_type
    context_object_name = 'servicedetail'


class ServiceDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Services_type
    success_url = reverse_lazy('dashboard:service_type_list')


# service video

class ServiceVideoListView (QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/service-video/list.html'
    model = Services_description
    context_object_name = 'servicevideo'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "description" in self.request.GET:
            if self.request.GET.get('description') != '':
                queryset = queryset.filter(
                    description__icontains=self.request.GET.get(
                        "description")
                )

        return queryset


class ServiceVideoCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/service-video/form.html'
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/service-video/form.html'
    model = Services_description
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/service-video/detail.html'
    model = Services_description
    context_object_name = 'servicevideodetail'


class ServiceVideoDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Services_description
    success_url = reverse_lazy('dashboard:service_video_list')


# contact

class ContactListView(QuerysetMixin, ListView):
    model = Contact
    template_name = 'dashboard/contact/list.html'
    context_object_name = 'contact'


class ContactCreateView(CreateView):
    template_name = 'dashboard/contact/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


class ContactUpdateView(UpdateView):
    template_name = 'dashboard/contact/form.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


class ContactDetailView(DetailView):
    template_name = 'dashboard/contact/detail.html'
    model = Contact
    context_object_name = 'contactdetail'


class ContactDeleteView(DeleteMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('dashboard:contact_list')


class RoomCommentListView(DashboardMixin, ListView):
    template_name = 'dashboard/room_comment/list.html'
    model = Comment
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(events__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "room" in self.request.GET:
            if self.request.GET.get('room') != '':
                queryset = queryset.filter(
                    room=self.request.GET.get("room"))
        return queryset


class RoomCommentCreateView(DashboardMixin, CreateView):
    template_name = 'dashboard/room_comment/form.html'
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


class RoomCommentUpdateView(DashboardMixin, UpdateView):
    template_name = 'dashboard/room_comment/form.html'
    model = Comment
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


class RoomCommentDetailView(DashboardMixin, DetailView):
    template_name = 'dashboard/room_comment/detail.html'
    model = Comment
    context_object_name = 'roomdetail'


class RoomCommentDeleteView(DeleteMixin, DashboardMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:room_comment_list')
