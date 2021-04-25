from django import forms
from .models import Room, News, Comment


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
        
class NewsCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('full_name','email', 'news','comment')
