from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.role = 'reader'
        if commit:
            user.save()
        return user 

class LoginUser(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=15,widget=forms.PasswordInput())