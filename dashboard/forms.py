from django import forms


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
