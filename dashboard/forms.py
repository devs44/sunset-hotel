from django import forms
from .models import Room, Event, Comment


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


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_type': forms.Select(attrs={
                'class': 'form-control select2',
                'placeholder': 'room type'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'price'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'choose image'
            })
        }

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
            'events' : forms.Select(attrs={
                'class' : 'form-control select2'
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

         