from django import forms
from django.contrib.auth.models import User
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=11)
    Country = forms.CharField(max_length=11)
    City = forms.CharField(max_length=11)
    email = forms.EmailField()
    student = forms.BooleanField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','phone','Country','City','student']


# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email']
#
#
# class ProfileUpadteForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
