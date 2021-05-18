from .mixin import *
from .forms import *
from django.shortcuts import render, redirect, reverse
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
        return redirect('/login/')


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/base/admindashboard.html'


# rooms
class RoomListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/room/roomlist.html'
    model = Room
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'room_list'

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


<<<<<<< HEAD
class RoomCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class RoomCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room/roomcreate.html'
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_create'

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


<<<<<<< HEAD
class RoomUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class RoomUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room/roomcreate.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_update'

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


<<<<<<< HEAD
class RoomDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class RoomDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room/roomdetail.html'
    model = Room
    context_object_name = 'roomdetail'
    login_url = '/login/'
    redirect_field_name = 'room_detail'

<<<<<<< HEAD
class RoomDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======

class RoomDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Room
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_list'

<<<<<<< HEAD
class RoomCategoryListView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======

class RoomCategoryListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_category/roomcategory.html'
    model = Room_Category
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'room_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "room_category" in self.request.GET:
            if self.request.GET.get('room_category') != '':
                queryset = queryset.filter(
                    title__contains=self.request.GET.get("room_category"))

        return queryset


<<<<<<< HEAD
class RoomCategoryCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class RoomCategoryCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')


<<<<<<< HEAD
class RoomCategoryUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class RoomCategoryUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    model = Room_Category
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')

# Feature


<<<<<<< HEAD
class FeatureListView(AdminRequiredMixin,DashboardMixin, QuerysetMixin, ListView):
=======
class FeatureListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/feature/feature.html'
    model = Feature
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'feature_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'room_feature' in self.request.GET:
            if self.request.GET.get('room_feature') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('room_feature')
                )
        return queryset


<<<<<<< HEAD
class FeatureCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class FeatureCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/feature/featurecreate.html'
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


<<<<<<< HEAD
class FeatureUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class FeatureUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/feature/featurecreate.html'
    model = Feature
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


<<<<<<< HEAD
class FeatureDeleteView(AdminRequiredMixin,DashboardMixin, DeleteMixin, DeleteView):
=======
class FeatureDeleteView(AdminRequiredMixin, DashboardMixin, DeleteMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Feature
    success_url = reverse_lazy('dashboard:feature_list')


<<<<<<< HEAD
class RoomCategoryDelete(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class RoomCategoryDelete(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_category/roomcategorydelete.html'
    model = Room_Category
    success_url = reverse_lazy('dashboard:room_category')


# Image
<<<<<<< HEAD
class ImageListView(AdminRequiredMixin,LoginRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class ImageListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/gallery/imagelist.html'
    model = RoomImage
    login_url = '/login/'
    redirect_field_name = 'image_list'


<<<<<<< HEAD
class ImageCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class ImageCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/gallery/imagecreate.html'
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


<<<<<<< HEAD
class ImageUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class ImageUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/gallery/imagecreate.html'
    model = RoomImage
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


<<<<<<< HEAD
class ImageDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class ImageDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = RoomImage
    success_url = reverse_lazy('dashboard:image_list')

# event


<<<<<<< HEAD
class EventListView(AdminRequiredMixin,DashboardMixin, QuerysetMixin, ListView):
=======
class EventListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event/eventlist.html'
    model = Event
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'event_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get("title"))
        return queryset


<<<<<<< HEAD
class EventCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class EventCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event/eventcreate.html'
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


<<<<<<< HEAD
class EventUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class EventUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event/eventcreate.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


<<<<<<< HEAD
class EventDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class EventDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event/eventdetail.html'
    model = Event
    context_object_name = 'eventdetail'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


<<<<<<< HEAD
class EventDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class EventDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Event
    success_url = reverse_lazy('dashboard:event_list')

# event comment


<<<<<<< HEAD
class EventCommentTemplateView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class EventCommentTemplateView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event_comment/eventcommentlist.html'
    model = Comment
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'eventcomment_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(room__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "full_name" in self.request.GET:
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name=self.request.GET.get("full_name"))
        return queryset


<<<<<<< HEAD
class EventCommentCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class EventCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


<<<<<<< HEAD
class EventCommentUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class EventCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    model = Comment
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


<<<<<<< HEAD
class EventCommentDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class EventCommentDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/event_comment/eventcommentdetail.html'
    model = Comment
    context_object_name = 'eventdetail'


<<<<<<< HEAD
class EventCommentDeleteView(AdminRequiredMixin,DeleteMixin, DeleteView):
=======
class EventCommentDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
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
<<<<<<< HEAD
class NewsListView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class NewsListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = News
    template_name = 'dashboard/news/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'news_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'title' in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('title')
                )
        return queryset


<<<<<<< HEAD
class NewsCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class NewsCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news/form.html'
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


<<<<<<< HEAD
class NewsUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class NewsUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news/form.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


<<<<<<< HEAD
class NewsDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class NewsDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news/detail.html'
    model = News
    context_object_name = 'newsdetail'


<<<<<<< HEAD
class NewsDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class NewsDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = News
    success_url = reverse_lazy('dashboard:news_list')


# newscomments

<<<<<<< HEAD
class NewsCommentTemplateView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class NewsCommentTemplateView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Comment
    template_name = 'dashboard/news_comment/list.html'
    context_object_name = 'news'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'news_comment_list'

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


<<<<<<< HEAD
class NewsCommentCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class NewsCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news_comment/form.html'
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


<<<<<<< HEAD
class NewsCommentUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class NewsCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news_comment/form.html'
    model = Comment
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


<<<<<<< HEAD
class NewsCommentDetailView(AdminRequiredMixin,DetailView):
=======
class NewsCommentDetailView(AdminRequiredMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/news_comment/detail.html'
    model = Comment
    context_object_name = 'commentdetail'


<<<<<<< HEAD
class NewsCommentDeleteView(AdminRequiredMixin,DeleteMixin, DeleteView):
=======
class NewsCommentDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Comment
    success_url = reverse_lazy('dashboard:news_comment_list')


# testimonial
<<<<<<< HEAD
class TestimonialListView(AdminRequiredMixin,QuerysetMixin, ListView):
=======
class TestimonialListView(AdminRequiredMixin, QuerysetMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Testomonial
    template_name = 'dashboard/testimonial/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'testimonial_list'

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


<<<<<<< HEAD
class TestimonialCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class TestimonialCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/testimonial/form.html'
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


<<<<<<< HEAD
class TestimonialUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class TestimonialUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/testimonial/form.html'
    model = Testomonial
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


<<<<<<< HEAD
class TestimonialDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class TestimonialDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/testimonial/detail.html'
    model = Testomonial
    context_object_name = 'testimonialdetail'


<<<<<<< HEAD
class TestimonialDeleteView(AdminRequiredMixin,DashboardMixin, DeleteMixin, DeleteView):
=======
class TestimonialDeleteView(AdminRequiredMixin, DashboardMixin, DeleteMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Testomonial
    success_url = reverse_lazy('dashboard:testimonial_list')

# message


<<<<<<< HEAD
class MessageListView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class MessageListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Message
    template_name = 'dashboard/message/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'message_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "email" in self.request.GET:
            queryset = queryset.filter(
                email=self.request.GET.get("email")
            )

        return queryset


<<<<<<< HEAD
class MessageCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class MessageCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/message/form.html'
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if user is not None:
            login(self.request, user)

        else:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid Username or password',
                              'form': form
                          })

        return super().form_valid(form)


<<<<<<< HEAD
class MessageUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class MessageUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/message/form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


<<<<<<< HEAD
class MessageDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class MessageDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/message/detail.html'
    model = Message
    context_object_name = 'messagedetail'


<<<<<<< HEAD
class MessageDeleteView(AdminRequiredMixin,DeleteMixin, DeleteView):
=======
class MessageDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Message
    success_url = reverse_lazy('dashboard:message_list')

# reservation


<<<<<<< HEAD
class ReservationListView(AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class ReservationListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Reservation
    template_name = 'dashboard/reservation/list.html'
    login_url = '/login/'
    redirect_field_name = 'reservation_list'

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


<<<<<<< HEAD
class ReservationCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class ReservationCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/reservation/form.html'
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')

    # def dispatch(self, request, *args, **kwargs):
    #     if 'frontend' in self.request.GET:
    #         self.success_url = reverse('reservation')

    #     return super().dispatch(request, *args, **kwargs)


<<<<<<< HEAD
class ReservationUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class ReservationUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/reservation/form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


<<<<<<< HEAD
class ReservationDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class ReservationDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/reservation/detail.html'
    model = Reservation
    context_object_name = 'reservationdetail'


<<<<<<< HEAD
class ReservationDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class ReservationDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Reservation
    success_url = reverse_lazy('dashboard:reservation_list')


class AboutView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/about/about.html'
    model = About
    paginate_by = 7

# About


<<<<<<< HEAD
class AboutCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class AboutCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:about_list')
    login_url = '/login/'
    redirect_field_name = 'about_list'


<<<<<<< HEAD
class AboutUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class AboutUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    model = About
    success_url = reverse_lazy('dashboard:about_list')


<<<<<<< HEAD
class AboutDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class AboutDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/about/aboutdetail.html'
    model = About
    context_object_name = 'aboutdetail'


<<<<<<< HEAD
class AboutDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class AboutDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = About
    success_url = reverse_lazy('dashboard:about_list')


# Service Type

<<<<<<< HEAD
class ServiceListView (AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class ServiceListView (AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/services-type/list.html'
    model = Services_type
    login_url = '/login/'
    redirect_field_name = 'service_type_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "service_type_name" in self.request.GET:
            if self.request.GET.get('service_type_name') != '':
                queryset = queryset.filter(
                    service_type_name__contains=self.request.GET.get(
                        "service_type_name")
                )

        return queryset


<<<<<<< HEAD
class ServiceCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class ServiceCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/services-type/form.html'
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


<<<<<<< HEAD
class ServiceUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class ServiceUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/services-type/form.html'
    model = Services_type
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


<<<<<<< HEAD
class ServiceDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class ServiceDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/services-type/detail.html'
    model = Services_type
    context_object_name = 'servicedetail'


<<<<<<< HEAD
class ServiceDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class ServiceDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Services_type
    success_url = reverse_lazy('dashboard:service_type_list')


# service video

<<<<<<< HEAD
class ServiceVideoListView (AdminRequiredMixin,QuerysetMixin, DashboardMixin, ListView):
=======
class ServiceVideoListView (AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/service-video/list.html'
    model = Services_description
    context_object_name = 'servicevideo'
    login_url = '/login/'
    redirect_field_name = 'service_video_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "description" in self.request.GET:
            if self.request.GET.get('description') != '':
                queryset = queryset.filter(
                    description__icontains=self.request.GET.get(
                        "description")
                )

        return queryset


<<<<<<< HEAD
class ServiceVideoCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class ServiceVideoCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/service-video/form.html'
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


<<<<<<< HEAD
class ServiceVideoUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class ServiceVideoUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/service-video/form.html'
    model = Services_description
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


<<<<<<< HEAD
class ServiceVideoDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class ServiceVideoDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/service-video/detail.html'
    model = Services_description
    context_object_name = 'servicevideodetail'


<<<<<<< HEAD
class ServiceVideoDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class ServiceVideoDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Services_description
    success_url = reverse_lazy('dashboard:service_video_list')


# contact

<<<<<<< HEAD
class ContactListView(AdminRequiredMixin,QuerysetMixin, ListView):
=======
class ContactListView(AdminRequiredMixin, QuerysetMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Contact
    template_name = 'dashboard/contact/list.html'
    context_object_name = 'contact'
    login_url = '/login/'
    redirect_field_name = 'contact_list'


<<<<<<< HEAD
class ContactCreateView(AdminRequiredMixin,CreateView):
=======
class ContactCreateView(AdminRequiredMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/contact/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


<<<<<<< HEAD
class ContactUpdateView(AdminRequiredMixin,UpdateView):
=======
class ContactUpdateView(AdminRequiredMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/contact/form.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


<<<<<<< HEAD
class ContactDetailView(AdminRequiredMixin,DetailView):
=======
class ContactDetailView(AdminRequiredMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/contact/detail.html'
    model = Contact
    context_object_name = 'contactdetail'


<<<<<<< HEAD
class ContactDeleteView(AdminRequiredMixin,DeleteMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('dashboard:contact_list')

# room comment
class RoomCommentListView(AdminRequiredMixin,DashboardMixin, ListView):
=======
class ContactDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('dashboard:contact_list')


class RoomCommentListView(AdminRequiredMixin, DashboardMixin, ListView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_comment/list.html'
    model = Comment
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'room_comment_lists'

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(events__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "room" in self.request.GET:
            if self.request.GET.get('room') != '':
                queryset = queryset.filter(
                    room=self.request.GET.get("room"))
        return queryset


<<<<<<< HEAD
class RoomCommentCreateView(AdminRequiredMixin,DashboardMixin, CreateView):
=======
class RoomCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_comment/form.html'
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


<<<<<<< HEAD
class RoomCommentUpdateView(AdminRequiredMixin,DashboardMixin, UpdateView):
=======
class RoomCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_comment/form.html'
    model = Comment
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


<<<<<<< HEAD
class RoomCommentDetailView(AdminRequiredMixin,DashboardMixin, DetailView):
=======
class RoomCommentDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    template_name = 'dashboard/room_comment/detail.html'
    model = Comment
    context_object_name = 'roomdetail'


<<<<<<< HEAD
class RoomCommentDeleteView(AdminRequiredMixin,DeleteMixin, DashboardMixin, DeleteView):
=======
class RoomCommentDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
>>>>>>> 1ee5982f31d8bd5a48cbe903bcc963c61084d3f7
    model = Comment
    success_url = reverse_lazy('dashboard:room_comment_list')
