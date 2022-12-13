from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput
from .models import *
from .choices import *
from django.utils.translation import gettext_lazy as _


class UserAddForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'user_type', 'first_name', 'last_name', 'driving_license']


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(label='New password', max_length=100, widget=forms.PasswordInput)
    new_password_repeat = forms.CharField(label='Repeat new password', max_length=100, widget=forms.PasswordInput)

    def clean_new_password_repeat(self):
        if self.cleaned_data.get('new_password') != self.cleaned_data.get('new_password_repeat'):
            raise ValidationError('The entered passwords are different!')
        return self.cleaned_data.get('new_password_repeat')


class AddressCompanyFromForm(ModelForm):
    class Meta:
        model = AddressCompanyFromModel
        fields = '__all__'
        labels = {
            'address_country': _('Country'),
            'address_city': _('City'),
            'address_zip_code': _('Zip code'),
            'address_street': _('Street'),
            'address_property_first': _('First line'),
            'address_property_second': _('Second line'),
            'address_more_info': _('More information'),
        }


class AddressCompanyToForm(ModelForm):
    class Meta:
        model = AddressCompanyToModel
        fields = '__all__'
        labels = {
            'address_country': _('Country'),
            'address_city': _('City'),
            'address_zip_code': _('Zip code'),
            'address_street': _('Street'),
            'address_property_first': _('First line'),
            'address_property_second': _('Second line'),
            'address_more_info': _('More information'),
        }


class TrailerForm(ModelForm):
    class Meta:
        model = TrailerModel
        fields = ['model', 'trailer_number', 'weighs', 'tons_can_load', 'cargo_space']
        help_texts = {
            'weighs': _('Weight in kilograms'),
            'tons_can_load': _('Weight in kilograms'),
            'cargo_space': _('Space for euro pallets'),
        }


class CarForm(ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        labels = {
            'have_to': _('Driver license'),
            'trailer': _('Assign trailer')
        }
        help_texts = {
            'have_to': _('What driving license should you drive'),
            'weighs': _('Weight in kilograms'),
            'tons_can_load': _('Weight in kilograms'),
            'cargo_space': _('Space for euro pallets'),
        }


class CargoForm(ModelForm):
    class Meta:
        model = CargoModel
        fields = '__all__'
        labels = {
            'have_to': _('Driver license'),
            'car_trailer_name': _('Assign trailer')
        }
        help_texts = {
            'have_to': _('What driving license should you drive'),
            'weighs': _('Weight in kilograms'),
            'pallets': _('How many pallets or goods'),
            'place_of_pallets': _('Space for euro pallets'),
        }


class PlanCargoForm(ModelForm):
    class Meta:
        model = PlanCargoModel
        fields = '__all__'


class DriverWorkerForm(ModelForm):
    class Meta:
        model = DriverWorkerModel
        fields = '__all__'
        labels = {
            'date': _('Date of departure'),
        }


class MessageForm(ModelForm):
    class Meta:
        model = MessageModel
        fields = '__all__'
