from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View

from .forms import StaffLoginForm
# Create your views here.


class LoginView(FormView):
    template_name = 'auth/login.html'
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
    template_name = 'base/admindashboard.html'


# rooms
