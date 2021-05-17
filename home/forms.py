from django.db.models import fields
from django.forms import ModelForm
from dashboard.models import Subscription

from dashboard.forms import FormControlMixin


class SubscriptionForm(FormControlMixin, ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attr.update({
            'placeholder': 'Email Address'
        })
