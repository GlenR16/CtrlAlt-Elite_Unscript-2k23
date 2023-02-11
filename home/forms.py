from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm,PasswordChangeForm
from .models import User
from django import forms
# Signup Form. Visible at /signup
class UserCreationForm(UserCreationForm):
    email = forms.EmailField(label="", required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    name = forms.CharField(label="", required=True,widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    password1 = forms.CharField(label="", required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label="", required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta(UserCreationForm):
        model = User
        fields = ('email','name')

# Change user password without old password. Don't use this.
class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','name')

# Login the user. Visible at /login
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="", required=True,widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label="", required=True,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ('email','password')

# Change user password with old password.
class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User