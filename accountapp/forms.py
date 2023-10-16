from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class AccountUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]

class CustomUserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',


            'first_name',
            'last_name',
            'email',
        ]