from django import forms
from .models import CheckoutInfo

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = CheckoutInfo
        fields = '__all__'

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)