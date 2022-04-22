from django import forms
from django.contrib.auth.forms import UserCreationForm

from ahc_app.models import User


class ClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64,
                             help_text='Enter a valid email address')
    mobile_number = forms.IntegerField(
        help_text='Enter a valid mobile number')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        if commit:
            user.save()
        return user


class SuperClientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64,
                             help_text='Enter a valid email address')
    mobile_number = forms.IntegerField(
        help_text='Enter a valid mobile number')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_super_client = True
        if commit:
            user.save()
        return user


class BrokerSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32, help_text='First name')
    last_name = forms.CharField(max_length=32, help_text='Last name')
    email = forms.EmailField(max_length=64,
                             help_text='Enter a valid email address')
    mobile_number = forms.IntegerField(
        help_text='Enter a valid mobile number')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile_number',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_broker = True
        if commit:
            user.save()
        return user
