from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Message

from django.contrib.auth.models import User, Group


class QuerysetMixin(object):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class DeleteMixin(object):
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class DashboardMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.filter(
            deleted_at__isnull=True).order_by("-id")
        return context


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_active and user.groups.filter(name="Admin").exists():

            pass
        else:
            return redirect('/login/')
            # raise PermissionDenied

        return super().dispatch(request, *args, *kwargs)


class SuperAdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if user.is_superuser:
            pass
        else:

            raise PermissionDenied

        return super().dispatch(request, *args, *kwargs)
