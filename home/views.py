from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from dashboard.models import *

from .mixin import *
from django.views.generic.edit import FormMixin
from dashboard.forms import *
# Create your views here.


class HomeTemplateView(BaseMixin, TemplateView):
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
        context['service'] = Services_type.objects.all()
        return context


class RoomListView(ListView):
    model = Room
    template_name = 'home/room/room.html'
    context_object_name = 'room'
    paginate_by = 4

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     if "arrival_date" in self.request.GET:
    #         if self.request.GET.get('arrival_date') != '':
    #             pass
    #     return queryset


class RoomDetailView(BaseMixin, DetailView):
    template_name = 'home/room/room_detail.html'
    model = Room

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.exclude(
            room_no=self.get_object().room_no)
        print(context['rooms'])
        context['feature'] = Feature.objects.all()

        return context

    # for posting review in selected room

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        room_no = self.kwargs.get('pk')
        room = Room.objects.get(room_no=room_no)
        obj = Comment.objects.create(
            full_name=name, email=email, room=room, comment=message)
        obj.save()
        return render(request, self.template_name)


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


class NewsDetailView(DetailView):
    template_name = 'home/news/news_detail.html'
    model = News
    form_class = NewsCommentForm
    context_object_name = "newsdetail"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.exclude(
            id=self.get_object().id).order_by("-id")
        print(context['news'])
        context['form'] = NewsCommentForm(initial={'news': self.object})
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('comment')
        news = self.kwargs.get('pk')
        form= News.objects.get(pk = news)
        obj = Comment.objects.create(
            full_name=name, email=email,website=website, comment=message, news = form)
        obj.save()
        return render(request, self.template_name)


class EventDetailView(DetailView):
    template_name = 'home/events/event_detail.html'
    model = Event
    form_class = EventCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.exclude(id=self.get_object().id)
        context['form'] = EventCommentForm(initial={'events': self.object})
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('comment')
        events = self.kwargs.get('pk')
        form= Event.objects.get(pk = events)
        obj = Comment.objects.create(
            full_name=name, email=email,website=website, comment=message, events = form)
        obj.save()
        return render(request, self.template_name)


class ContactTemplateView(BaseMixin, TemplateView):
    model = Contact
    template_name = 'home/contact/contact.html'
    form_class = MessageForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MessageForm()
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form= Message.objects.get(pk = message)
        obj = Message.objects.create(
            full_name=name, email=email, message=message)
        obj.save()
        return render(request, self.template_name)


class EventListView(ListView):
    model = Event
    template_name = 'home/events/event.html'
    context_object_name = 'event'
    paginate_by = 3
    context_object_name = 'event'
