from email.mime.text import MIMEText
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
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from django.db.models import Q

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

    def get_queryset(self):
        queryset = super().get_queryset()

        children = self.request.GET.get('children')
        adults = self.request.GET.get('adults')

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
                messages.success(
                    self.request, "Welcome"
                )
            elif arrival_date < datetime.date.today():
                messages.error(
                    self.request, "Sorry, please select valid date.")
                queryset = ''
            if arrival_date > departure_date:
                messages.error(
                    self.request, "Sorry, invalid arrival and departure date.")
                queryset = ''
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feature'] = Feature.objects.all()
        return context


class RoomDetailView(BaseMixin, QuerysetMixin, DetailView):
    template_name = 'home/room/room_detail.html'
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
        return redirect('room_detail', pk=room_no)
   
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


class ReservationView(BaseMixin, TemplateView):
    template_name = 'home/reservation/reservation.html'
    form_class = ReservationForm

    def get_initial(self):
        initial = {}
        initial['check_in_date'] = timezone.now().date()
        return initial

    def get_form(self):
        print(self.form_class)

        return self.form_class(initial=self.get_initial())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "room_id" in self.request.GET:
            context['selected_room'] = Room.objects.filter(
                room_no=self.request.GET.get('room_id')).first()
        context['rooms'] = Room.objects.filter(deleted_at__isnull=True)
        context['form'] = self.get_form()
        return context

    # def form_valid(self, form):
    #     check_in = form.cleaned_data['check_in_date']
    #     check_out = form.cleaned_data['check_out_date']
    #     adults = form.cleaned_data['adult']
    #     children = form.cleaned_data['children']
    #     first_name = form.cleaned_data['first_name']
    #     last_name = form.cleaned_data['last_name']
    #     email = form.cleaned_data['email']
    #     phone = form.cleaned_data['phone']
    #     address1 = form.cleaned_data['address_1']
    #     address2 = form.cleaned_data['address_2']
    #     state = form.cleaned_data['state']
    #     city = form.cleaned_data['city']
    #     country = form.cleaned_data['country']
    #     zip_code = form.cleaned_data['zip_code']
    #     special_req = form.cleaned_data['special_req']
    #     print(check_in, 333333333333)
    #     obj = Reservation.objects.create(
    #         first_name=first_name, last_name=last_name,
    #         check_in_date=check_in, check_out_date=check_out, adult=adults, children=children,
    #         email=email, phone=phone, address_1=address1, address_2=address2, city=city,
    #         country=country, state=state, zip_code=zip_code, special_req=special_req)

    #     if "room_id" in self.request.GET:
    #         room_no = Room.objects.get(room_no=self.request.GET.get('room_id'))
    #         obj.selected_room = room_no

    #         obj.save(update_fields=['selected_room'])
    #         room_no.checked_in_date = check_in
    #         room_no.checked_out_date = check_out
    #         room_no.availability = False
    #         room_no.save()

    #     if form.cleaned_data['selected_room']:
    #         room_no = Room.objects.get(
    #             room_no=form.cleaned_data['selected_room'])
    #         obj.selected_room = room_no
    #         obj.save(update_fields=['selected_room'])
    #         room_no.checked_in_date = check_in
    #         room_no.checked_out_date = check_out
    #         room_no.availability = False
    #         room_no.save()
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     check_in = request.POST.get('check_in_date')
    #     check_out = request.POST.get('check_out_date')
    #     adults = request.POST.get('adult')
    #     children = request.POST.get('children')
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     email = request.POST.get('email')
    #     phone = request.POST.get('phone')
    #     address1 = request.POST.get('address_1')
    #     address2 = request.POST.get('address_2')
    #     state = request.POST.get('state')
    #     city = request.POST.get('city')
    #     country = request.POST.get('country')
    #     zip_code = request.POST.get('zip_code')
    #     special_req = request.POST.get('special_req')
    #     obj = Reservation.objects.create(
    #         first_name=first_name, last_name=last_name,
    #         check_in_date=check_in, check_out_date=check_out, adult=adults, children=children,
    #         email=email, phone=phone, address_1=address1, address_2=address2, city=city,
    #         country=country, state=state, zip_code=zip_code, special_req=special_req)
    #     if "room_id" in self.request.GET:
    #         room_no = Room.objects.get(room_no=self.request.GET.get('room_id'))
    #         obj.selected_room = room_no

    #         obj.save(update_fields=['selected_room'])
    #         room_no.checked_in_date = check_in
    #         room_no.checked_out_date = check_out
    #         room_no.availability = False
    #         room_no.save()

    #     if request.POST.get('selected_room'):
    #         room_no = Room.objects.get(
    #             room_no=request.POST.get('selected_room'))
    #         obj.selected_room = room_no
    #         obj.save(update_fields=['selected_room'])
    #         room_no.checked_in_date = check_in
    #         room_no.checked_out_date = check_out
    #         room_no.availability = False
    #         room_no.save()
    #     return redirect(reverse_lazy('reservation'))


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
    template_name = 'home/news/news_detail.html'
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
            full_name=name, email=email,website=website, comment=message, news = form)
    
        return redirect('news_detail', pk=news)


class EventDetailView(DetailView):
    template_name = 'home/events/event_detail.html'
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
            full_name=name, email=email,website=website, comment=message, events = form)
        return redirect('event_detail', pk=events)

        


class ContactTemplateView(BaseMixin, TemplateView):
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

        obj = Message.objects.create(
            full_name=name, email=email, message=message)
        return redirect('contact')
    
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        print(email, 1111111)
        if "@" in email:
            pass

        else:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid Username or password',
                              'form': form
                          })

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
    model = RoomImage
    template_name = 'home/gallery/gallery.html'
    context_object_name = 'photo'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SingleRoomListView(ListView):
    model = RoomImage
    template_name = 'home/gallery/single room.html'
    context_object_name = 'photo'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single'] = Image.objects.filter(
            image_type__title="Single Room")
        context['si'] = Room.objects.filter(
            room_type__title="Single Room")
    
        return context


class DoubleRoomListView(ListView):
    model = RoomImage
    template_name = 'home/gallery/double room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['double'] = Image.objects.filter(
            image_type__title="Double Room")
        context['si'] = Room.objects.filter(
            room_type__title="Double Room")
        return context



class DeluxeRoomListView(ListView):
    model = RoomImage
    template_name = 'home/gallery/deluxe room.html'
 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deluxe'] = Image.objects.filter(
            image_type__title="Deluxe Room")
        context['royal'] = Image.objects.filter(image_type__title="Royal Room")

        return context

class RoyalRoomListView(ListView):
    model = RoomImage
    template_name = 'home/gallery/royal room.html'
 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['royal'] = Image.objects.filter(
            image_type__title="Royal Room")
        context['si'] = Room.objects.filter(
            room_type__title="Royal Room")
        return context


class NewsletterView(CreateView):
    
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_email'] = Subscription.objects.create(email=user_email)
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        admin_email = admin_info.email
        send_mail("asdasdas", msg, conf_settings.EMAIL_HOST_USER,
                  [email], fail_silently=True)
        redirect('home:home')


# class SearchView(ListView):
#     template_name = 'home/search/search.html'
#     model = Room

#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         if 'keyword' in request.GET:
#             keyword = request.GET['key']