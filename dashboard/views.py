from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, View, ListView, CreateView, UpdateView, DeleteView

from .models import Room, Event, Comment, RoomImage, News

from .forms import StaffLoginForm, RoomForm, EventForm, EventCommentForm, NewsForm


# Create your views here.


class QuerysetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


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
            if self.request.GET.get('room_no') != None and self.request.GET.get('room_no') != '':
                queryset = queryset.filter(
                    room_no=self.request.GET.get("room_no"))
        if "room_type" in self.request.GET:
            queryset = queryset.filter(
                room_type__title__contains=self.request.GET.get("room_type")
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


class RoomDeleteView(DeleteView):
    template_name = 'dashboard/room/roomdelete.html'
    model = Room
    success_url = reverse_lazy('dashboard:room_list')

class EventListView(ListView):
    template_name = 'dashboard/event/eventlist.html'
    model = Event

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

class EventDelteView(DeleteView):
    template_name = 'dashboard/event/eventdelete.html'
    model = Event
    success_url = reverse_lazy('dashboard:event_list')

#eventcomment
class EventCommentListView(ListView):
    template_name = 'dashboard/event_comment/eventcommentlist.html'
    model = Comment

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

class EventCommentDelteView(DeleteView):
    template_name = 'dashboard/event_comment/eventcommentdelete.html'
    model = Comment
    success_url = reverse_lazy('dashboard:event_list')
    def form_valid(self, form):
        pk = form.save()
        pk.delete()
        return super().form_valid(form)


class RoomSearchView(View):
    def get(self, request, *args, **kwargs):
        room = request.GET.get('room_search')
        queryset = Room.objects.all()
        if room:
            queryset = queryset.filter(room_type__icontains=room)
        return queryset
# news


class NewsListView(ListView):
    model = News
    template_name = 'dashboard/news/news.html'


class NewsCreateView(CreateView):
    template_name = 'dashboard/news/newscreate.html'
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsUpdateView(UpdateView):
    template_name = 'dashboard/news/newscreate.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsDetailView(DetailView):
    template_name = 'dashboard/news/newsdetail.html'
    model = News
    context_object_name = 'newsdetail'


class NewsDeleteView(DeleteView):
    template_name = 'dashboard/news/newsdelete.html'
    model = News
    success_url = reverse_lazy('dashboard:news_list')
