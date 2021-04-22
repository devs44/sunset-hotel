from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name =  'home/base/index.html'

class ReservationView(TemplateView):
    template_name = 'home/reservation/reservation.html'