from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from dashboard.models import *

from django.views.generic.edit import FormMixin
from dashboard.forms import *
# Create your views here.


class HomeTemplateView(TemplateView):
    model = Room
    template_name = 'home/base/index.html'
    # context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Image.objects.all()
        context['room'] = Room.objects.all()
        context['news'] = News.objects.all().order_by("-id")
        context['event'] = Event.objects.all()
        context['test'] = Testomonial.objects.all()
        context['contact'] = Contact.objects.filter(deleted_at__isnull=True).order_by('-id')
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'home/room/room.html'
    context_object_name = 'room'


class RoomDetailView(DetailView):
    template_name = 'home/room/room_detail.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.exclude(room_no=self.get_object().room_no)
        print(context['rooms'])
        return context


class ServiceListView(ListView):
    model = Services_description
    template_name = 'home/about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services_type.objects.all()
        context['test'] = Testomonial.objects.all()
        context['serve'] = Services_description.objects.all()
        context['ser'] = Services_type.objects.all()
        context['about'] = About.objects.all()
        return context


class ReservationView(TemplateView):
    template_name = 'home/reservation/reservation.html'


class NewsListView(ListView):
    template_name = 'home/news/list.html'
    model = News
    context_object_name = "news"
        
    

class NewsDetailView(FormMixin,DetailView):
    template_name = 'home/news/news_detail.html'
    model = News
    form_class = NewsCommentForm
    context_object_name = "newsdetail"

    def get_success_url(self):
        return redirect('news_detail', kwargs={'id': self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.exclude(
            id=self.get_object().id).order_by("-id")
        print(context['news'])
        context['form'] = NewsCommentForm(initial={'news': self.object})
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
        
    def form_valid(self, form):
        form.save()
        return super(NewsDetailView, self).form_valid(form)
    

class EventDetailView(DetailView):
    template_name = 'home/events/event_detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.exclude(id=self.get_object().id)
        print(context['events'])
        return context

class ContactTemplateView(TemplateView):
    model = Contact
    template_name = 'home/contact/contact.html'

    