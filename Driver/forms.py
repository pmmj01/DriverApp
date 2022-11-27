from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import UserModel, AddressCompanyFromModel, AddressCompanyToModel, DriverModel, ForwarderModel, \
    TrailerModel, CarModel, CargoModel, PlanCargoModel, DriverWorkerModel, MessageModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'


def login_validator(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError('This login already exists!')


class AddUserForm(forms.Form):
    login = 'phone_number'
    phone_regex = RegexValidator(regex=r'^(\+\d{2,3})?\d{9,11}$',
                                 message='Phone number must be entered in the format: "+00000000000". Up to 14 digits allowed.')
    phone_number = forms.CharField(validators=[phone_regex], max_length=15, blank=False, primary_key=True)
    password = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    password_repeat = forms.CharField(label='Password', max_length=100, widget=forms.PasswordInput)
    name = forms.CharField(label='Name', max_length=64)
    surname = forms.CharField(label='Surname', max_length=64)

    def clean_login(self):
        if User.objects.filter(username=self.cleaned_data.get('login')).exists():
            raise ValidationError('This login already exists!')
        return self.cleaned_data.get('login')

    def clean_password_repeat(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_repeat'):
            raise ValidationError('The entered passwords are different!')
        return self.cleaned_data.get('password_repeat')


class AddressCompanyFromForm(ModelForm):
    class Meta:
        model = AddressCompanyFromModel
        fields = '__all__'


class AddressCompanyToForm(ModelForm):
    class Meta:
        model = AddressCompanyToModel
        fields = '__all__'


class DriverForm(ModelForm):
    class Meta:
        model = DriverModel
        fields = '__all__'


class ForwarderForm(ModelForm):
    class Meta:
        model = ForwarderModel
        fields = '__all__'


class TrailerForm(ModelForm):
    class Meta:
        model = TrailerModel
        fields = '__all__'


class CarForm(ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'


class CargoForm(ModelForm):
    class Meta:
        model = CargoModel
        fields = '__all__'


class PlanCargoForm(ModelForm):
    class Meta:
        model = PlanCargoModel
        fields = '__all__'


class DriverWorkerForm(ModelForm):
    class Meta:
        model = DriverWorkerModel
        fields = '__all__'


class MessageForm(ModelForm):
    class Meta:
        model = MessageModel
        fields = '__all__'
