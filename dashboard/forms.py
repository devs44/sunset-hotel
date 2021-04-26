from django import forms
from .models import Room, News, Comment, Event, Testomonial, Message, Reservation, Room_Category, Feature, Image


class FormControlMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[fields].widget.attrs.update({
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
                'class': 'form-control',
                'placeholder': 'room no'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'price'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
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

            'Created By': forms.Select(attrs={
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
        fields = ('full_name', 'email', 'news', 'comment')


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control select2',
                'placeholder': 'event title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),
            'created_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'created by'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }


class EventCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
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
            'created_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'created by'
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
                'placeholder': 'voice'
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
            'check_in_date' : forms.DateTimeInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'check in date'
            }),
            'check_out_date' : forms.DateTimeInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'check out date'
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
        print(adult,111111111111111111111111)
        return adult
    # def __init__(self, *args, **kwargs):
    #     super(EventCommentForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Name'
    #     })
    #     self.fields['email_address'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Please enter your valid email address'
    #     })
    #     self.fields['website'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Please enter your website'
    #     })
    #     self.message['message'].widget.attrs.update({
    #         'class': 'form-control',
    #         'placeholder': 'Please enter your message'
    #     })
