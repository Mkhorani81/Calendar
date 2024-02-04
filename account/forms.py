from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import CaptchaField


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'password1', 'password2')


class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField()


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True

    class Meta:
        model = UserInfo
        fields = ('username', 'email', 'first_name', 'last_name')
