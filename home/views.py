from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from django.core.mail import send_mail
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from dashboard.models import *

from .mixin import *
from dashboard.mixin import DeleteMixin, QuerysetMixin
from django.views.generic.edit import FormMixin
from dashboard.forms import *
from email.mime.text import MIMEText
# Create your views here.


class HomeTemplateView(BaseMixin, TemplateView):
    model = Room
    template_name = 'home/base/index.html'
    # context_object_name = 'room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = Image.objects.all()
        context['room'] = Room.objects.filter(deleted_at__isnull=True)
        context['news'] = News.objects.all().order_by("-id")
        context['event'] = Event.objects.all()
        context['test'] = Testomonial.objects.all()
        context['service'] = Services_type.objects.all()
        return context


class RoomListView(QuerysetMixin, ListView):
    model = Room
    template_name = 'home/room/room.html'
    context_object_name = 'room'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['features'] = Feature.objects.all()
        return context


class RoomDetailView(BaseMixin, QuerysetMixin, DetailView):
    template_name = 'home/room/room_detail.html'
    model = Room

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
    form_class = ReservationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "room_id" in self.request.GET:
            context['selected_room'] = Room.objects.filter(
                room_no=self.request.GET.get('room_id')).first()
        context['rooms'] = Room.objects.filter(deleted_at__isnull=True)
        return context

    # def form_valid(self,form):
    #     check_in = form.cleaned_data['check-in']

    def post(self, request, *args, **kwargs):
        check_in = request.POST.get('check-in')
        check_out = request.POST.get('check-out')
        adults = request.POST.get('form-adults')
        children = request.POST.get('form-children')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address1 = request.POST.get('address-line1')
        address2 = request.POST.get('address-line2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip-code')
        special_req = request.POST.get('requirements')
        obj = Reservation.objects.create(
            first_name=first_name, last_name=last_name,
            check_in_date=check_in, check_out_date=check_out, adult=adults, children=children,
            email=email, phone=phone, address_1=address1, address_2=address2, city=city,
            country=country, state=state, zip_code=zip_code, special_req=special_req)
        if "room_id" in self.request.GET:
            room_no = Room.objects.get(room_no=self.request.GET.get('room_id'))
            obj.selected_room = room_no
            obj.save(update_fields=['selected_room'])
        if request.POST.get('room-no'):
            room_no = Room.objects.get(room_no=request.POST.get('room-no'))
            obj.selected_room = room_no
            obj.save(update_fields=['selected_room'])
        return render(request, self.template_name)


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


class GalleryListView(ListView):
    model = RoomImage
    template_name = 'home/gallery/gallery.html'
    context_object_name = 'photo'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single'] = Image.objects.filter(
            image_type__title="Single Room")
        context['double'] = Image.objects.filter(
            image_type__title="Double Room")
        context['deluxe'] = Image.objects.filter(
            image_type__title="Deluxe Room")
        context['royal'] = Image.objects.filter(image_type__title="Royal Room")
        
        return context



class NewsletterView(CreateView):
    template_name = 'home/base/footer.html'
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_email'] = Subscription.objects.create(email=user_email)
        return context

    msg = MIMEText('body of your message')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail("asdasdas", msg, conf_settings.EMAIL_HOST_USER, [email], fail_silently=True)
        redirect('home:home')
    