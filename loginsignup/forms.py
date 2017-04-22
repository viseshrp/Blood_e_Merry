from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from loginsignup.models import Donor


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Provide a valid email address.')
    phone = forms.CharField(required=True, help_text='Required.')
    city = forms.CharField(required=True, help_text='Required.')
    state = forms.CharField(required=True, help_text='Required.')
    country = forms.CharField(required=True, help_text='Required.')

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'phone',
            'city',
            'state',
            'country',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
