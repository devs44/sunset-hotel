from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from dashboard.models import Contact


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(). get_context_data()
        context['contact'] = Contact.objects.filter(deleted_at__isnull = True).order_by('-id')
        return context



   
      

       
        

    

    
