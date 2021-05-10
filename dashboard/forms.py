from django import forms
from .models import *
from django.contrib import messages
from django.core.exceptions import ValidationError

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

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if username in Account.objects.all():
    #         return username
    #     else:
    #         raise ValidationError('')


class RoomForm(FormControlMixin, forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control select2',
        'multiple': True

    }))

    class Meta:
        model = Room
        fields = '__all__'
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
            'image': forms.ClearableFileInput(attrs={
                'placeholder': 'choose image'
            }),


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
        exclude = ['deleted_at','events','room']
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
        exclude = ['deleted_at', 'news','room']
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
                'class': 'form-control select2',
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
            'email': forms.TextInput(attrs={
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
        print(email, 1111111111111111)
        if '@' in email:
            pass
        else:
            raise ValidationError('enter valid email')
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
                'class': 'form-control',
                'placeholder': 'check in date'
            }),
            'check_out_date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'check out date'
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

    def clean_adult(self):
        adult = self.cleaned_data['adult']
        print(adult, 111111111111111111111111)
        return adult


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
        exclude = ['deleted_at','events','news']
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
