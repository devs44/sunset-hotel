from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from .models import Room, News

from .forms import StaffLoginForm, RoomForm, NewsForm
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


#news

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

    