from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from .models import Room, News, Comment, RoomImage, Event, Room_Category, Feature, Image, Testomonial, Message, Reservation, Services_type, Services_description, Contact,  About
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView, DetailView, FormView, View, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template import loader
from django.http import JsonResponse
from .forms import *
from .mixin import *
from django.views import generic
from django.http.response import HttpResponseRedirect


# from django.contrib import messages


# Create your views here.


class LoginView(FormView):
    template_name = 'dashboard/auth/login.html'
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
        return redirect('/login/')


class PasswordsChangeView(PasswordChangeView):
    template_name = 'dashboard/password/password_change.html'
    form_class = ChangePasswordForm
    success_url = reverse_lazy('dashboard:admin_login')

    def get_form(self):
        form = super().get_form()
        form.set_user(self.request.user)
        return form

    def form(self, form):
        old_password = form.cleaned_data['old_password']

        if check_password(old_password, request.user.password):
            messages.add_message(request, messages.ERROR, "invalid pass")


# class PasswordResetView(FormView):
#     template_name = 'auth/password_reset.html'
#     success_url ='auth/login'
#     form_class = PasswordResetRequestForm()

#     def form_valid(self,*args,**kwargs):
#         form = super(PasswordResetView, self).form_vlaid(*args, **kwargs)
#         data = form.cleaned_data['email_or_username']
#         user = User.objects.filter(Q(email= data) |
#                                    Q(username = data)).first()
#         if user:
#             c = {
#                 'email': user.email,
#                 'domain': self.request.META['HTTP_HOST'],
#                 'site_name': 'your site',
#                 'password' :
#                 'user': user,
#                 'token': default_token_generator.make_token(user),
#                 'protocol': self.request.scheme,
#             }

#             email_template_name='registration/password_reset_email.html'
#             subject = "Reset Your Password"
#             email = loader.render_to_string(email_tempplate_name, c)
#             send_mail(subject, email, DEFAULT_FROM_EMAIL, [user.email], fail_silently = False)
#         messages.success(self.request, 'An email has been sent to ' + data +" if it is a valid user.")
#         return form


class PasswordResetView(FormView):
    template_name = 'dashboard/auth/reset-password.html'
    # form_class = PasswordResetForm
    success_url = reverse_lazy('dashboard:user_list')

    def dispatch(self, request, *args, **kwargs):

        if 'reset' in self.request.GET:
            self.success_url = reverse('dashboard:admin_login')

    #     return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        code = get_random_string(8)
        user = User.objects.get(email=email)

        text_content = 'Please use the code to reset your password. '
        send_mail(
            'Password Reset | Sunset Hotels',
            text_content +
            code,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        messages.success(
            self.request, "Password reset code is sent to " + email + ".")
        user.set_password(code)
        user.save()
        return super(). form_valid(form)


class AdminDashboardView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/base/admindashboard.html'


class UserCreateView(SuperAdminRequiredMixin, AdminRequiredMixin, CreateView):
    template_name = 'dashboard/users/usercreate.html'
    form_class = UserForm
    success_url = reverse_lazy('dashboard:user_list')

    def form_valid(self, form):
        print('form valid method called')
        return super().form_valid(form)

    # def form_valid(self, form):
    #     print('form valid method called')
    #     password = get_random_string(8)
    #     email = form.cleaned_data['email']
    #     username = form.cleaned_data['username']
    #     first_name = form.cleaned_data['first_name']
    #     last_name = form.cleaned_data['last_name']
    #     joined_date = form.cleaned_data['date_joined']
    #     print(email, username, password, first_name, last_name, joined_date)
    #     text = f'''username : {email}
    #     password : {password}
    #     '''
    #     send_mail(
    #         "Your login credentials: ",
    #         text +
    #         settings.EMAIL_HOST_USER,
    #         [email],
    #         fail_silently=False
    #     )
    #     return super(UserCreateView, self).form_valid(form)


class UsersListView(SuperAdminRequiredMixin, AdminRequiredMixin, ListView):
    template_name = 'dashboard/users/userlist.html'
    login_url = '/login/'
    redirect_field_name = reverse_lazy('dashboard:user_list')
    paginate_by = 5

    def get_queryset(self):
        return User.objects.all()

# rooms


class RoomListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/room/roomlist.html'
    model = Room
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'room_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "room_no" in self.request.GET:
            if self.request.GET.get('room_no') != '':
                queryset = queryset.filter(
                    room_no=self.request.GET.get("room_no"))
        if "room_type" in self.request.GET:
            if self.request.GET.get('room_type') != '':
                queryset = queryset.filter(
                    room_type__title__contains=self.request.GET.get(
                        "room_type")
                )
        if "price" in self.request.GET:
            if self.request.GET.get('price') != '':
                queryset = queryset.filter(
                    price=self.request.GET.get("price")
                )

        return queryset


class RoomCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/room/roomcreate.html'
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_create'

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


class RoomImageCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    model = RoomImage
    form_class = RoomImageForm
    template_name = "dashboard/layouts/form.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.is_ajax():
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse({"error": "Cannot access this page"}, status=404)

    def form_valid(self, form):
        instance = form.save()
        return JsonResponse(
            {
                "status": "ok",
                "pk": instance.pk,
                "url": instance.photo.url,
            }
        )

    def form_invalid(self, form):
        return JsonResponse({"errors": form.errors}, status=400)


class RoomUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/room/roomcreate.html'
    model = Room
    form_class = RoomForm
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_update'

    def form_valid(self, form):
        room = form.save()
        images = self.request.FILES.getlist('more_images')
        for img in images:
            RoomImage.objects.create(room=room, image=img)
        return super().form_valid(form)


class RoomDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/room/roomdetail.html'
    model = Room
    context_object_name = 'roomdetail'
    login_url = '/login/'
    redirect_field_name = 'room_detail'


class RoomDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Room
    success_url = reverse_lazy('dashboard:room_list')
    login_url = '/login/'
    redirect_field_name = 'room_list'


class RoomCategoryListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/room_category/roomcategory.html'
    model = Room_Category
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'room_category'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "room_category" in self.request.GET:
            if self.request.GET.get('room_category') != '':
                queryset = queryset.filter(
                    title__contains=self.request.GET.get("room_category"))

        return queryset


class RoomCategoryCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')


class RoomCategoryUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/room_category/roomcategorycreate.html'
    model = Room_Category
    form_class = RoomCategoryForm
    success_url = reverse_lazy('dashboard:room_category')

# Feature


class FeatureListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/feature/feature.html'
    model = Feature
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'feature_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'room_feature' in self.request.GET:
            if self.request.GET.get('room_feature') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('room_feature')
                )
        return queryset


class FeatureCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/feature/featurecreate.html'
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/feature/featurecreate.html'
    model = Feature
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:feature_list')


class FeatureDeleteView(AdminRequiredMixin, DashboardMixin, DeleteMixin, DeleteView):
    model = Feature
    success_url = reverse_lazy('dashboard:feature_list')


class RoomCategoryDelete(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    template_name = 'dashboard/room_category/roomcategorydelete.html'
    model = Room_Category
    success_url = reverse_lazy('dashboard:room_category')


# Image
class ImageListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/gallery/imagelist.html'
    model = RoomImage
    login_url = '/login/'
    redirect_field_name = 'image_list'


class ImageCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/gallery/imagecreate.html'
    model = RoomImage
    form_class = ImageForm
    success_url = reverse_lazy('dashboard:image_list')


class ImageDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = RoomImage
    success_url = reverse_lazy('dashboard:image_list')

# event


class EventListView(AdminRequiredMixin, DashboardMixin, QuerysetMixin, ListView):
    template_name = 'dashboard/event/eventlist.html'
    model = Event
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'event_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get("title"))
        return queryset


class EventCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/event/eventcreate.html'
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/event/eventcreate.html'
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('dashboard:event_list')


class EventDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/event/eventdetail.html'
    model = Event
    context_object_name = 'eventdetail'

    def get_object(self):
        obj = super().get_object()
        obj.view_count += 1
        obj.save()
        return obj


class EventDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('dashboard:event_list')

# event comment


class EventCommentTemplateView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/event_comment/eventcommentlist.html'
    model = Comment
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'eventcomment_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(room__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "full_name" in self.request.GET:
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name=self.request.GET.get("full_name"))
        return queryset


class EventCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/event_comment/eventcommentcreate.html'
    model = Comment
    form_class = EventCommentForm
    success_url = reverse_lazy('dashboard:eventcomment_list')


class EventCommentDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/event_comment/eventcommentdetail.html'
    model = Comment
    context_object_name = 'eventdetail'


class EventCommentDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:eventcomment_list')


class RoomSearchView(View):
    def get(self, request, *args, **kwargs):
        room = request.GET.get('room_search')
        queryset = Room.objects.all()
        if room:
            queryset = queryset.filter(room_type__icontains=room)
        return queryset


# news
class NewsListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    model = News
    template_name = 'dashboard/news/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'news_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'title' in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    title__icontains=self.request.GET.get('title')
                )
        return queryset


class NewsCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/news/form.html'
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/news/form.html'
    model = News
    form_class = NewsForm
    success_url = reverse_lazy('dashboard:news_list')


class NewsDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/news/detail.html'
    model = News
    context_object_name = 'newsdetail'


class NewsDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = News
    success_url = reverse_lazy('dashboard:news_list')


# newscomments

class NewsCommentTemplateView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    model = Comment
    template_name = 'dashboard/news_comment/list.html'
    context_object_name = 'news'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'news_comment_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(events__isnull=True),
                                                 Q(room__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if 'full_name' in self.request.GET:
            if self.request.GET.get('full_name') != '':
                queryset = queryset.filter(
                    full_name__icontains=self.request.GET.get('full_name')
                )
        return queryset


class NewsCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/news_comment/form.html'
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/news_comment/form.html'
    model = Comment
    form_class = NewsCommentForm
    success_url = reverse_lazy('dashboard:news_comment_list')


class NewsCommentDetailView(AdminRequiredMixin, DetailView):
    template_name = 'dashboard/news_comment/detail.html'
    model = Comment
    context_object_name = 'commentdetail'


class NewsCommentDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:news_comment_list')


# testimonial
class TestimonialListView(AdminRequiredMixin, QuerysetMixin, ListView):
    model = Testomonial
    template_name = 'dashboard/testimonial/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'testimonial_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "name" in self.request.GET:
            if self.request.GET.get('name') != '':
                queryset = queryset.filter(
                    name__icontains=self.request.GET.get('name')
                )
        if "profession" in self.request.GET:
            queryset = queryset.filter(
                profession__icontains=self.request.GET.get("profession")
            )

        return queryset


class TestimonialCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/testimonial/form.html'
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/testimonial/form.html'
    model = Testomonial
    form_class = TestimonialForm
    success_url = reverse_lazy('dashboard:testimonial_list')


class TestimonialDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/testimonial/detail.html'
    model = Testomonial
    context_object_name = 'testimonialdetail'


class TestimonialDeleteView(AdminRequiredMixin, DashboardMixin, DeleteMixin, DeleteView):
    model = Testomonial
    success_url = reverse_lazy('dashboard:testimonial_list')

# message


class MessageListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    model = Message
    template_name = 'dashboard/message/list.html'
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'message_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "email" in self.request.GET:
            queryset = queryset.filter(
                email=self.request.GET.get("email")
            )

        return queryset


class MessageCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/message/form.html'
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if user is not None:
            login(self.request, user)

        else:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid Username or password',
                              'form': form
                          })

        return super().form_valid(form)


class MessageUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/message/form.html'
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('dashboard:message_list')


class MessageDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/message/detail.html'
    model = Message
    context_object_name = 'messagedetail'


class MessageDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('dashboard:message_list')

# reservation


class ReservationListView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    model = Reservation
    template_name = 'dashboard/reservation/list.html'
    login_url = '/login/'
    redirect_field_name = 'reservation_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "first_name" in self.request.GET:
            if self.request.GET.get('first_name') != '':
                queryset = queryset.filter(
                    first_name=self.request.GET.get("first_name"))
        if "selected_room" in self.request.GET:
            if self.request.GET.get('selected_room') != '':
                queryset = queryset.filter(
                    selected_room=self.request.GET.get(
                        "selected_room")
                )
        if "check_in_date" in self.request.GET:
            if self.request.GET.get('check_in_date') != '':
                queryset = queryset.filter(
                    check_in_date=self.request.GET.get("check_in_date")
                )

        return queryset


class ReservationCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/reservation/form.html/'
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')

    # def dispatch(self, request, *args, **kwargs):
    #     if 'frontend' in self.request.GET:
    #         self.success_url = reverse('reservation')

    #     return super().dispatch(request, *args, **kwargs)


class ReservationUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/reservation/form.html'
    model = Reservation
    form_class = ReservationForm
    success_url = reverse_lazy('dashboard:reservation_list')


class ReservationDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/reservation/detail.html'
    model = Reservation
    context_object_name = 'reservationdetail'


class ReservationDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Reservation
    success_url = reverse_lazy('dashboard:reservation_list')


class AboutView(AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/about/about.html'
    model = About
    paginate_by = 7

# About


class AboutCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:about_list')
    login_url = '/login/'
    redirect_field_name = 'about_list'


class AboutUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/about/aboutcreate.html'
    form_class = AboutForm
    model = About
    success_url = reverse_lazy('dashboard:about_list')


class AboutDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/about/aboutdetail.html'
    model = About
    context_object_name = 'aboutdetail'


class AboutDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = About
    success_url = reverse_lazy('dashboard:about_list')


# Service Type

class ServiceListView (AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/services-type/list.html'
    model = Services_type
    login_url = '/login/'
    redirect_field_name = 'service_type_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "service_type_name" in self.request.GET:
            if self.request.GET.get('service_type_name') != '':
                queryset = queryset.filter(
                    service_type_name__contains=self.request.GET.get(
                        "service_type_name")
                )

        return queryset


class ServiceCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/services-type/form.html'
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/services-type/form.html'
    model = Services_type
    form_class = ServiceTypeForm
    success_url = reverse_lazy('dashboard:service_type_list')


class ServiceDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/services-type/detail.html'
    model = Services_type
    context_object_name = 'servicedetail'


class ServiceDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Services_type
    success_url = reverse_lazy('dashboard:service_type_list')


# service video

class ServiceVideoListView (AdminRequiredMixin, QuerysetMixin, DashboardMixin, ListView):
    template_name = 'dashboard/service-video/list.html'
    model = Services_description
    context_object_name = 'servicevideo'
    login_url = '/login/'
    redirect_field_name = 'service_video_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        if "description" in self.request.GET:
            if self.request.GET.get('description') != '':
                queryset = queryset.filter(
                    description__icontains=self.request.GET.get(
                        "description")
                )

        return queryset


class ServiceVideoCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/service-video/form.html'
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/service-video/form.html'
    model = Services_description
    form_class = ServiceVideoForm
    success_url = reverse_lazy('dashboard:service_video_list')


class ServiceVideoDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/service-video/detail.html'
    model = Services_description
    context_object_name = 'servicevideodetail'


class ServiceVideoDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Services_description
    success_url = reverse_lazy('dashboard:service_video_list')


# contact

class ContactListView(AdminRequiredMixin, QuerysetMixin, ListView):
    model = Contact
    template_name = 'dashboard/contact/list.html'
    context_object_name = 'contact'
    login_url = '/login/'
    redirect_field_name = 'contact_list'


class ContactCreateView(AdminRequiredMixin, CreateView):
    template_name = 'dashboard/contact/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


class ContactUpdateView(AdminRequiredMixin, UpdateView):
    template_name = 'dashboard/contact/form.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contact_list')


class ContactDetailView(AdminRequiredMixin, DetailView):
    template_name = 'dashboard/contact/detail.html'
    model = Contact
    context_object_name = 'contactdetail'


class ContactDeleteView(AdminRequiredMixin, DeleteMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('dashboard:contact_list')

# room comment


class RoomCommentListView(AdminRequiredMixin, DashboardMixin, ListView):
    template_name = 'dashboard/room_comment/list.html'
    model = Comment
    paginate_by = 5
    login_url = '/login/'
    redirect_field_name = 'room_comment_lists'

    def get_queryset(self):
        queryset = super().get_queryset().filter(Q(news__isnull=True),
                                                 Q(events__isnull=True) &
                                                 Q(deleted_at__isnull=True))
        if "room" in self.request.GET:
            if self.request.GET.get('room') != '':
                queryset = queryset.filter(
                    room=self.request.GET.get("room"))
        return queryset


class RoomCommentCreateView(AdminRequiredMixin, DashboardMixin, CreateView):
    template_name = 'dashboard/room_comment/form.html'
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


class RoomCommentUpdateView(AdminRequiredMixin, DashboardMixin, UpdateView):
    template_name = 'dashboard/room_comment/form.html'
    model = Comment
    form_class = RoomCommentForm
    success_url = reverse_lazy('dashboard:room_comment_list')


class RoomCommentDetailView(AdminRequiredMixin, DashboardMixin, DetailView):
    template_name = 'dashboard/room_comment/detail.html'
    model = Comment
    context_object_name = 'roomdetail'


class RoomCommentDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('dashboard:room_comment_list')


# newsletter

class NewsletterListView(AdminRequiredMixin, DashboardMixin, ListView):
    template_name = 'dashboard/newsletter/list.html'
    model = Subscription
    context_object_name = 'email'


class NewsletterDeleteView(AdminRequiredMixin, DeleteMixin, DashboardMixin, DeleteView):
    model = Subscription
    success_url = reverse_lazy('dashboard:newsletter_list')
