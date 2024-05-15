from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())

    password1 = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    phone = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=100, required=True, widget=forms.EmailInput())
    city = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    house = forms.CharField(max_length=100, required=True, widget=forms.TextInput())
    postal_code = forms.CharField(max_length=100, required=True, widget=forms.TextInput())

    def save(self, commit=True):
        user = super().save(commit=False)  # Get the user instance without saving it yet
        user.email = self.cleaned_data['email']
        user.save()  # Save the user instance

        profile = Profile.objects.create(user=user,
                                         first_name=self.cleaned_data['first_name'],
                                         last_name=self.cleaned_data['last_name'],
                                         email=self.cleaned_data['email'],
                                         phone=self.cleaned_data['phone'],
                                         city=self.cleaned_data['city'],
                                         house=self.cleaned_data['house'],
                                         postal_code=self.cleaned_data['postal_code'],
        )

        return user

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name',
                  'last_name', 'phone', 'email', 'city', 'house', 'postal_code']



class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    phone = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput())
    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput())
    city = forms.CharField(max_length=100,
                              required=True,
                              widget=forms.TextInput())
    house = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput())
    postal_code = forms.CharField(max_length=100,
                           required=True,
                           widget=forms.TextInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'email', 'city', 'house', 'postal_code']
