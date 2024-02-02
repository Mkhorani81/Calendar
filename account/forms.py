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