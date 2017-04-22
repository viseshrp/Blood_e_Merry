from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from loginsignup.models import Donor


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Provide a valid email address.', max_length=30)
    phone = forms.CharField(required=True, help_text='Required.', max_length=10)
    city = forms.CharField(required=True, help_text='Required.', max_length=30)
    state = forms.CharField(required=True, help_text='Required.',  max_length=30)
    country = forms.CharField(required=True, help_text='Required.', max_length=30)
    blood_group = forms.CharField(required=True, help_text='Required. Example: B+', max_length=2)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
            'blood_group',
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
