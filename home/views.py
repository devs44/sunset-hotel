from django.shortcuts import render
from django.views.generic import ListView,TemplateView, DetailView
from dashboard.models import *
# Create your views here.

class HomeTemplateView(TemplateView):
    model = Room
    template_name = 'home/base/index.html'
    # context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Image.objects.all()  
        context['room'] = Room.objects.all()      
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
        context['rooms'] = Room.objects.exclude(id=self.get_object().id)
        print(context['rooms'])
        return context

class ServiceListView(ListView):
    model = Services_description
    template_name = 'home/about/about.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services_type.objects.all()

        return context

class ReservationView(TemplateView):
    template_name = 'home/reservation/reservation.html'