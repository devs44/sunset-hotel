from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from .models import Room, Event, Comment

from .forms import StaffLoginForm, RoomForm, EventForm, EventCommentForm
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
class RoomListView(ListView):
    template_name = 'dashboard/room/roomlist.html'
    model = Room


class RoomCreateView(CreateView):
    template_name = 'dashboard/room/roomcreate.html'
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')


class RoomUpdateView(UpdateView):
    template_name = 'dashboard/room/roomcreate.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')


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