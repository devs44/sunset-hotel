from django import forms
from .models import Room, News, Comment, Event, Room_Category, Feature, Image


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
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control select2',
        'multiple': True
    }))

    class Meta:
        model = Room
        fields = '__all__'
        widgets = {
            'room_type': forms.Select(attrs={
                'class': 'form-control select2',
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
