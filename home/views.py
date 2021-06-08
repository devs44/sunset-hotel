from email.mime.text import MIMEText

from django.conf import settings
from django.http.response import StreamingHttpResponse

from django.views.generic.base import View

# to send email with template
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template

from home.forms import SubscriptionForm

from django.core.validators import validate_email
from dashboard.forms import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormMixin
from dashboard.mixin import DeleteMixin, QuerysetMixin
from .mixin import *
from dashboard.models import *
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.core.mail import send_mail
from django.views.generic import ListView, TemplateView, DetailView
from django.contrib import messages
from dateutil.parser import parse as parse_date
from django.urls import reverse_lazy
import datetime
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.db.models import Count, Sum


# Create your views here.


class HomeTemplateView(BaseMixin, TemplateView):
    model = Room
    template_name = 'home/base/index.html'
    form_class = MessageForm
    # context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Image.objects.all()
        context['room'] = Room.objects.filter(deleted_at__isnull=True)
        context['news'] = News.objects.all().order_by("-id")
        context['event'] = Event.objects.all()
        context['test'] = Testomonial.objects.all()
        context['service'] = Services_type.objects.all()
        context['about'] = About.objects.all()
        context['form'] = MessageForm()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = Message.objects.create(
            full_name=name, email=email, message=message)
        return redirect('home')


class RoomListView(QuerysetMixin, ListView):
    model = Room
    template_name = 'home/room/room.html'
    context_object_name = 'room'
    paginate_by = 4

    def dispatch(self, request, *args, **kwargs):
        if 'departure_date' and 'arrival_date' in self.request.GET:
            departure_date = parse_date(
                self.request.GET.get('departure_date')).date()
            arrival_date = parse_date(
                self.request.GET.get('arrival_date')).date()
            if arrival_date < datetime.date.today():
                messages.error(
                    self.request, "Sorry, please select valid date.")
                return HttpResponseRedirect(reverse('home'))
            elif arrival_date > departure_date:
                messages.error(
                    self.request, "Sorry, invalid arrival and departure date.")
                return HttpResponseRedirect(reverse('home'))
        return super().dispatch(request, *args, *kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if 'departure_date' in self.request.GET and 'arrival_date' in self.request.GET:
            departure_date = parse_date(
                self.request.GET.get('departure_date')).date()
            arrival_date = parse_date(
                self.request.GET.get('arrival_date')).date()
            # timezon.now().date() instead of datetime

            if arrival_date != '' and departure_date != '' and arrival_date >= datetime.date.today():
                queryset = queryset.filter(
                    Q(checked_in_date__isnull=True, checked_out_date__isnull=True) |
                    Q(checked_out_date__lte=arrival_date) |
                    Q(checked_in_date__gte=departure_date))
                if queryset.count() < 1:
                    messages.success(self.request, "We are really sorry")
                else:
                    messages.success(
                        self.request, "Welcome"
                    )
        if 'adults' in self.request.GET or 'children' in self.request.GET:
            children = int(self.request.GET.get('children'))
            adults = int(self.request.GET.get('adults'))
            if children == 1 and adults <= 2:
                queryset = queryset.filter(Q(room_type__title="Single Room") |
                                           Q(room_type__title='Double Room'))
            else:
                queryset = queryset.all().exclude(room_type__title='Single Room')
        if 'keyword' in self.request.GET:
            if self.request.GET.get('keyword') != '':
                search_item = self.request.GET.get('keyword')
                queryset = queryset.filter(Q(room_type__title__contains=search_item) |
                                           Q(room_no__contains=search_item) |
                                           Q(price__contains=search_item) |
                                           Q(description__contains=search_item))

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature'] = Feature.objects.all()
        return context


class RoomDetailView(BaseMixin, QuerysetMixin, DetailView):
    template_name = 'home/room/event-detail.html'
    model = Room
    form_class = RoomCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rooms'] = Room.objects.exclude(
            room_no=self.get_object().room_no)
        room_no = self.kwargs.get('pk')
        context['feature'] = Feature.objects.all()
        context['reviews'] = Comment.objects.filter(Q(deleted_at__isnull=True) &
                                                    Q(news__isnull=True) &
                                                    Q(events__isnull=True) &
                                                    Q(room=room_no)).order_by('-id')
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
        messages.success(request, "Comment added!")
        return redirect('room-detail', pk=room_no)


class ServiceListView(TemplateView):
    model = About
    template_name = 'home/about/about.html'

    def get_context_data(self, **kwargs):
        adult = Reservation.objects.all().aggregate(
            total_adult=Sum('adult'))['total_adult']
        children = Reservation.objects.all().aggregate(
            total_children=Sum('children'))['total_children']
        context = super().get_context_data(**kwargs)
        context['services'] = Services_type.objects.all()
        context['test'] = Testomonial.objects.all()
        context['serve'] = Services_description.objects.all()
        context['ser'] = Services_type.objects.all()
        context['about'] = About.objects.all()
        context['room_count'] = Room.objects.count()

        context['guests'] = adult + children
        return context

class ReservationView(BaseMixin, CreateView):
    template_name = 'home/reservation/reservation.html'
    form_class = ReservationForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super(ReservationView, self).get_context_data(**kwargs)
        form = ReservationForm(self.request.POST or None)
        if "room_id" in self.request.GET:
            context['selected_room'] = Room.objects.filter(
                room_no=self.request.GET.get('room_id')).first()
        context['rooms'] = Room.objects.filter(deleted_at__isnull=True)
        return context

    def get_initial(self):
        initial = super().get_initial()
        if "room_id" in self.request.GET:
            room = Room.objects.filter(
                room_no=self.request.GET.get('room_id')).first()
            initial['selected_room'] = room.pk

            return initial

    def form_valid(self, form):
        if 'room_id' in self.request.GET:
            selected_room = get_object_or_404(
                Room, room_no=self.request.GET.get('room_id'))
            # getting form instance and saving selected room
            form.instance.selected_room = selected_room
        if form.is_valid():
            messages.success(self.request, "your reservation is success!")
            if 'room_id' in self.request.GET and self.request.GET.get('room_id') != '' or 'selected_room' in self.request.POST and self.request.POST.get('selected_room'):
                obj = Room.objects.get(Q(room_no=self.request.GET.get('room_id')) |
                                       Q(room_no=self.request.POST.get('selected_room')))
                departure_date = parse_date(
                    self.request.POST.get('check_out_date')).date()
                arrival_date = parse_date(
                    self.request.POST.get('check_in_date')).date()
                obj.checked_in_date = arrival_date
                obj.checked_out_date = departure_date
                obj.availability = False
                obj.save()
        return super().form_valid(form)


class NewsListView(ListView):
    template_name = 'home/news/list.html'
    model = News
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.kwargs.get('pk')
        context['comments_count'] = Comment.objects.filter(news=news).count()
        return context


class NewsDetailView(DetailView):
    template_name = 'home/news/news-detail.html'
    model = News
    form_class = NewsCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.exclude(
            id=self.get_object().id).order_by("-id")
        context['form'] = NewsCommentForm(initial={'news': self.object})
        news = self.kwargs.get('pk')
        context['comment'] = Comment.objects.filter(news=news).order_by('-id')
        context['comments_count'] = Comment.objects.filter(news=news).count()

        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('comment')
        news = self.kwargs.get('pk')
        form = News.objects.get(pk=news)
        obj = Comment.objects.create(
            full_name=name, email=email, website=website, comment=message, news=form)

        return redirect('news-detail', pk=news)


class EventDetailView(DetailView):
    template_name = 'home/events/event-detail.html'
    model = Event
    form_class = EventCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.exclude(id=self.get_object().id)
        context['form'] = EventCommentForm(initial={'events': self.object})
        events = self.kwargs.get('pk')
        context['comment'] = Comment.objects.filter(
            events=events).order_by('-id')
        context['comments_count'] = Comment.objects.filter(
            events=events).count()
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('comment')
        events = self.kwargs.get('pk')
        form = Event.objects.get(pk=events)
        obj = Comment.objects.create(
            full_name=name, email=email, website=website, comment=message, events=form)
        return redirect('event-detail', pk=events)


class ContactTemplateView(BaseMixin, CreateView):
    template_name = 'home/contact/contact.html'
    form_class = MessageForm
    success_url = reverse_lazy('contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = MessageForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = Message.objects.create(
            full_name=name, email=email, message=message)
        return redirect('contact')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if "@" not in email:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid Username or password',
                              'form': form
                          })
        else:
            pass
        return super().form_valid(form)


class EventListView(ListView):
    model = Event
    template_name = 'home/events/event.html'
    context_object_name = 'event'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = self.kwargs.get('pk')
        context['comments_count'] = Comment.objects.filter(
            events=events).count()
        return context


class GalleryListView(ListView):
    model=Image
    template_name = 'home/gallery/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = Image.objects.filter(deleted_at__isnull=True)
        context['roomtitle'] = Room_Category.objects.all()
        return context


# class SearchView(ListView):
#     template_name = 'home/search/search.html'
#     model = Room

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if 'keyword' in request.GET:
#             keyword = request.GET['key']

class SubscriptionView(View):
    def post(self, request, *args, **kwargs):
        email = self.request.POST.get('s_email')
        if Subscription.objects.filter(email=email).exists():
            messages.warning(request, "Wow, Already Subscribed.")

        else:
            obj = Subscription.objects.create(email=email)
            messages.success(
                request, f'Thank you for Subscription {email}')
            subject = "Thank you for joining Us"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]
            # with open(settings.BASE_DIR / "/home/dreamer26/django/hotel ms/hotelproject/hms/home/templates/home/newsletter/newsletter.txt") as f:
            #     signup_message = f.read()
            html_template = get_template(
                "home/newsletter/newsletter.html").render()
            plain_text = get_tabemplate(
                "home/newsletter/newsletter.txt").render()
            message = EmailMultiAlternatives(
                subject, plain_text, from_email, to_email)

            message.attach_alternative(html_template, "text/html")
            message.send()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class UnSubscriptionView(View):
    def post(self, request, *args, **kwargs):
        email = self.request.GET.get('email')
        if Subscription.objects.filter(email=email).exists():
            Subscription.objects.filter(email=email).delete()
            messages.success(request, "Sorry to let you go")
        else:
            messages.error(request, "Invalid email address")
        return HttpResponseRedirect(self.request.path_info)


class SearchView(TemplateView):
    template_name = 'home/search/search-result.html'
