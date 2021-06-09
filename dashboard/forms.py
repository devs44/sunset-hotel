import datetime

from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget
from django.db.models import fields
from django.forms import widgets
from django.utils.translation import gettext as _

from .models import *


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({

                'class': 'form-control'

            })


class StaffLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            pass
        else:
            raise ValidationError({
                'username': 'Invalid username or password'
            })


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder':  'Password'}))

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder':  'Password'}))

    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder':  'Password'}))

    def set_user(self, user):
        self.user = user

    def clean(self):
        old_password = self.cleaned_data.get('old_password')
        valpwd = self.cleaned_data.get('new_password1')
        valrpwd = self.cleaned_data.get('new_password2')

        if valpwd != valrpwd:
            raise forms.ValidationError({
                'new_password1': 'Password Not Matched'})

        else:
            pass
        return self.cleaned_data


class RoomImageForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = RoomImage
        fields = ['image']


class RoomForm(FormControlMixin, forms.ModelForm):

    class Meta:
        model = Room
        fields = ['room_type', 'room_no', 'description',
                  'checked_in_date', 'checked_out_date', 'availability', 'price', 'image', 'features']
        widgets = {
            'room_type': forms.Select(attrs={
                'class': 'select2',
                'placeholder': 'room type'
            }),
            'room_no': forms.TextInput(attrs={
                'placeholder': 'room no'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'description'
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'price'
            }),

            "availability": DjangoToggleSwitchWidget(klass="django-toggle-switch-success"),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['features'].widget.attrs.update({
            'class': 'form-control select2 feature-select',
            'multiple': 'multiple'
        })


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            }),

            'created_by': forms.Select(attrs={
                'class': 'form-control select2',
            })

        }


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = Room_Category
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Room category here...'
            })
        }


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'room feature...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        widgets = {
            'image_type': forms.Select(attrs={
                'class': 'form-control select2',
            }),
            'caption': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'caption...'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            })
        }


class NewsCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['deleted_at', 'events', 'room']
        widgets = {
            'news': forms.Select(attrs={
                'class': 'form-control select2'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website'
            }),
            'created_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'created by'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter message'
            })
        }


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'title'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            }),

            'created_by': forms.Select(attrs={
                'class': 'form-control select2',
            })

        }


class EventCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['deleted_at', 'news', 'room']
        widgets = {
            'events': forms.Select(attrs={
                'class': 'form-control select2'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website'
            }),
            'created_by': forms.Select(attrs={
                'class': 'form-control select2',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter message'
            })
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testomonial
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name'
            }),
            'profession': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'profession'
            }),
            'voice': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'feedback'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message'
            })
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if '@' not in email:
            raise forms.ValidationError('Enter valid email')
        return email


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        exclude = ['deleted_at']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your last name'
            }),
            'selected_room': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your room'
            }),
            'adult': forms.Select(attrs={
                'class': 'form-control',
            }),
            'check_in_date': forms.DateTimeInput(attrs={
                'class': 'form-control check-date',
                'placeholder': datetime.date.today()
            }),
            'check_out_date': forms.DateTimeInput(attrs={
                'class': 'form-control check-date',
                'placeholder': datetime.date.today()
            }),
            'children': forms.Select(attrs={
                'class': 'form-control select2',

            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number'
            }),
            'address_1': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone address_1'
            }),
            'address_2': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone address_2'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your state '
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your city'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your zip_code'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your country'
            }),
            'special_req': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your special request'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['children'].choices = self.fields['children'].choices[1:]
        self.fields['adult'].choices = self.fields['adult'].choices[1:]

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = self.cleaned_data.get('check_in_date').date()
        check_out_date = self.cleaned_data.get('check_out_date').date()
        selected_room = self.cleaned_data.get('selected_room')
        if check_in_date == '' or check_out_date == '' or selected_room == '':
            raise ValidationError('This field is required')
        if check_in_date != None or check_out_date != None:
            if check_in_date > check_out_date:
                raise ValidationError({
                    "check_in_date": "Invalid check-in check-out date"})

        room = Room.objects.filter(room_no=selected_room).first()
        check_in = room.checked_in_date
        check_out = room.checked_out_date
        if check_in_date >= check_in and check_in_date < check_out:
            raise ValidationError({
                'check_in_date': 'This room is not available at this date'
            })
        if check_out_date > check_in and check_out_date < check_out:
            raise ValidationError({
                'check_out_date': 'This room is not available at this time.'
            })
        if check_in_date < check_in and check_out_date <= check_out:
            raise ValidationError({
                'check_out_date': 'This room is not available at this time.'
            })


class AboutForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'


class ServiceTypeForm(forms.ModelForm):
    class Meta:
        model = Services_type
        fields = '__all__'
        widgets = {
            'service_type_name': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'Service type'
            }),
            'service_type_description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Service description'
            }),
            'service_png': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }


class ServiceVideoForm(forms.ModelForm):
    class Meta:
        model = Services_description
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'service_video': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose Video'
            })
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'

            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Address'
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone number'
            }),
            'fax': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Fax'
            })
        }


class RoomCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['deleted_at', 'events', 'news']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'Enter name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'created_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'created by'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter review'
            })
        }


class PasswordResetForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter email address'
    }))

    def clean_email(self):
        e = self.cleaned_data.get('email')
        if Account.objects.filter(email=e).exists():
            pass
        else:
            raise forms.ValidationError("User with this email doesn't exist")

        return e


class UserForm(FormControlMixin, forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'address', 'image', 'mobile', 'groups']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'onchange': 'preview()'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].widget.attrs.update(
            {'class': 'form-control select2 feature-select'})

    def clean(self):
        cleaned_data = super().clean()
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        mobile = self.cleaned_data['mobile']
        if Account.objects.filter(username=username).exists():
            raise ValidationError({
                'username': 'this username is not available'
            })
        if Account.objects.filter(email=email).exists():
            raise ValidationError({
                'email': 'user with this email already exists'
            })
        if Account.objects.filter(mobile=mobile):
            raise ValidationError({
                'mobile': 'user with this mobile no. already exists'
            })
        if len(mobile) < 10:
            raise ValidationError({
                'mobile': 'Invalid mobile no.'
            })
