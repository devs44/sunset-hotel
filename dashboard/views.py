from .mixin import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

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


class AdminDashboardView(TemplateView):
    template_name = 'dashboard/base/admindashboard.html'


# rooms
class RoomListView(QuerysetMixin, ListView):
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


class RoomCreateView(CreateView):
    template_name = 'dashboard/room/roomcreate.html'
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


class RoomUpdateView(UpdateView):
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


class RoomDetailView(DetailView):
    template_name = 'dashboard/room/roomdetail.html'
    model = Room
    context_object_name = 'roomdetail'


class RoomDeleteView(DeleteMixin, DeleteView):
    template_name = 'dashboard/room/roomdelete.html'
    model = Room
    success_url = reverse_lazy('dashboard:room_list')


class RoomCategoryListView(QuerysetMixin, ListView):
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


class RoomCategoryCreateView(CreateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')


class RoomCategoryUpdateView(UpdateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    model = Room_Category
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')

# Feature


class FeatureListView(QuerysetMixin, ListView):
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


class FeatureCreateView(CreateView):
    template_name = 'dashboard/feature/featurecreate.html'
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureUpdateView(UpdateView):
    template_name = 'dashboard/feature/featurecreate.html'
    model = Feature
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureDeleteView(DeleteView):
    template_name = 'dashboard/feature/featuredelete.html'
    model = Feature
    success_url = reverse_lazy('dashboard:feature_list')


class RoomCategoryDelete(DeleteMixin, DeleteView):
    template_name = 'dashboard/room_category/roomcategorydelete.html'
    model = Room_Category
    success_url = reverse_lazy('dashboard:room_category')


# Image
class ImageListView(QuerysetMixin, ListView):
    template_name = 'dashboard/gallery/imagelist.html'
    model = Image


class ImageCreateView(CreateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageUpdateView(UpdateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    model = Image
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageDeleteView(DeleteMixin, DeleteView):
    template_name = 'dashboard/gallery/imagedelete.html'
    model = Image
    success_url = reverse_lazy('dashboard:image_list')


class EventListView(ListView):
    template_name = 'dashboard/event/eventlist.html'
    model = Event

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get("title"))
        return queryset


class EventCreateView(CreateView):
    template_name = 'dashboard/event/eventcreate.html'
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventUpdateView(UpdateView):
    template_name = 'dashboard/event/eventcreate.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventDetailView(DetailView):
    template_name = 'dashboard/event/eventdetail.html'
    model = Event
    context_object_name = 'eventdetail'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class EventDeleteView(DeleteView):
    template_name = 'dashboard/event/eventdelete.html'
    model = Event
    success_url = reverse_lazy('dashboard:event_list')

# event comment


class EventCommentTemplateView(ListView):
    template_name = 'dashboard/event_comment/eventcommentlist.html'
    model = Comment
    
    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True) &
            Q(deleted_at__isnull=True))
        if "full_name" in self.request.GET:
            print(queryset,1111111111111)
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name=self.request.GET.get("full_name"))
        return queryset


class EventCommentCreateView(CreateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentUpdateView(UpdateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    model = Comment
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentDetailView(DetailView):
    template_name = 'dashboard/event_comment/eventcommentdetail.html'
    model = Comment
    context_object_name = 'eventdetail'


class EventCommentDeleteView(DeleteMixin, DeleteView):
    template_name = 'dashboard/event_comment/eventcommentdelete.html'
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
class NewsListView(QuerysetMixin, ListView):
    model = News
    template_name = 'dashboard/news/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'title' in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('title')
                )
        return queryset


class NewsCreateView(CreateView):
    template_name = 'dashboard/news/form.html'
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsUpdateView(UpdateView):
    template_name = 'dashboard/news/form.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsDetailView(DetailView):
    template_name = 'dashboard/news/detail.html'
    model = News
    context_object_name = 'newsdetail'


class NewsDeleteView(DeleteMixin, DeleteView):
    template_name = 'dashboard/news/delete.html'
    model = News
    success_url = reverse_lazy('dashboard:news_list')


# newscomments

class NewsCommentTemplateView(TemplateView):
    model = Comment
    template_name = 'dashboard/news_comment/list.html'
    form_class = 'NewsForm'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Comment.objects.filter(events__isnull=True)
        return context


class NewsCommentCreateView(CreateView):
    template_name = 'dashboard/news_comment/form.html'
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentUpdateView(UpdateView):
    template_name = 'dashboard/news_comment/form.html'
    model = Comment
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentDetailView(DetailView):
    template_name = 'dashboard/news_comment/detail.html'
    model = Comment
    context_object_name = 'commentdetail'


class NewsCommentDeleteView(DeleteView):
    template_name = 'dashboard/news_comment/delete.html'
    model = Comment
    success_url = reverse_lazy('dashboard:news_comment_list')


# testimonial
class TestimonialListView(QuerysetMixin, ListView):
    model = Testomonial
    template_name = 'dashboard/testimonial/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "name" in self.request.GET:
            if self.request.GET.get('name') != None and self.request.GET.get('name') != '':
                queryset = queryset.filter(
                    room_no=self.request.GET.get("name"))
        if "profession" in self.request.GET:
            queryset = queryset.filter(
                room_type__title__contains=self.request.GET.get("profession")
            )

        return queryset


class TestimonialCreateView(CreateView):
    template_name = 'dashboard/testimonial/form.html'
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialUpdateView(UpdateView):
    template_name = 'dashboard/testimonial/form.html'
    model = Testomonial
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialDetailView(DetailView):
    template_name = 'dashboard/testimonial/detail.html'
    model = Testomonial
    context_object_name = 'testimonialdetail'


class TestimonialDeleteView(DeleteView):
    template_name = 'dashboard/testimonial/delete.html'
    model = Testomonial
    success_url = reverse_lazy('dashboard:testimonial_list')

# message


class MessageListView(QuerysetMixin, ListView):
    model = Message
    template_name = 'dashboard/message/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()

        if "email" in self.request.GET:
            queryset = queryset.filter(
                email=self.request.GET.get("email")
            )

        return queryset


class MessageCreateView(CreateView):
    template_name = 'dashboard/message/form.html'
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


class MessageUpdateView(UpdateView):
    template_name = 'dashboard/message/form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


class MessageDetailView(DetailView):
    template_name = 'dashboard/message/detail.html'
    model = Message
    context_object_name = 'messagedetail'


class MessageDeleteView(DeleteView):
    template_name = 'dashboard/message/delete.html'
    model = Message
    success_url = reverse_lazy('dashboard:message_list')

# reservation


class ReservationListView(QuerysetMixin, ListView):
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


class ReservationCreateView(CreateView):
    template_name = 'dashboard/reservation/form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


class ReservationUpdateView(UpdateView):
    template_name = 'dashboard/reservation/form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


class ReservationDetailView(DetailView):
    template_name = 'dashboard/reservation/detail.html'
    model = Reservation
    context_object_name = 'reservationdetail'


class ReservationDeleteView(DeleteView):
    template_name = 'dashboard/reservation/delete.html'
    model = Reservation
    success_url = reverse_lazy('dashboard:reservation_list')


class AboutView(QuerysetMixin, ListView):
    template_name = 'dashboard/about/about.html'
    model = About
    paginate_by = 7

# About


class AboutCreateView(CreateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:about_list')


class AboutUpdateView(UpdateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    model = About
    success_url = reverse_lazy('dashboard:about_list')


class AboutDetailView(DetailView):
    template_name = 'dashboard/about/aboutdetail.html'
    model = About
    context_object_name = 'aboutdetail'


class AboutDeleteView(DeleteMixin, DeleteView):
    template_name = 'dashboard/about/aboutdelete.html'
    model = About
    success_url = reverse_lazy('dashboard:about_list')


# Service Type

class ServiceListView (ListView):
    template_name = 'dashboard/services-type/list.html'
    model = Services_type
    context_object_name = 'servicetype'


class ServiceCreateView(CreateView):
    template_name = 'dashboard/services-type/form.html'
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceUpdateView(UpdateView):
    template_name = 'dashboard/services-type/form.html'
    model = Services_type
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceDetailView(DetailView):
    template_name = 'dashboard/services-type/detail.html'
    model = Services_type
    context_object_name = 'servicedetail'


class ServiceDeleteView(DeleteView):
    template_name = 'dashboard/services-type/delete.html'
    model = Services_type
    success_url = reverse_lazy('dashboard:service_type_list')


# service video

class ServiceVideoListView (ListView):
    template_name = 'dashboard/service-video/list.html'
    model = Services_description
    context_object_name = 'servicevideo'


class ServiceVideoCreateView(CreateView):
    template_name = 'dashboard/service-video/form.html'
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoUpdateView(UpdateView):
    template_name = 'dashboard/service-video/form.html'
    model = Services_description
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoDetailView(DetailView):
    template_name = 'dashboard/service-video/detail.html'
    model = Services_description
    context_object_name = 'servicevideodetail'


class ServiceVideoDeleteView(DeleteView):
    template_name = 'dashboard/services-video/delete.html'
    model = Services_description
    success_url = reverse_lazy('dashboard:service_video_list')
    

#contact

class ContactListView(ListView):
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


class ContactDeleteView(DeleteView):
    template_name = 'dashboard/contact/delete.html'
    model = Contact
    success_url = reverse_lazy('dashboard:contact_list')
    

    
