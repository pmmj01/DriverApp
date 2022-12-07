from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import UserModel, AddressCompanyFromModel, AddressCompanyToModel, DriverModel, ForwarderModel, \
    TrailerModel, CarModel, CargoModel, PlanCargoModel, DriverWorkerModel, MessageModel


class AddUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'user_type', 'first_name', 'last_name']

    def clean_login(self):
        if UserModel.objects.filter(phone_number=self.cleaned_data.get('login')).exists():
            raise ValidationError('This login already exists!')
        return self.cleaned_data.get('login')

    def clean_password_repeat(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_repeat'):
            raise ValidationError('The entered passwords are different!')
        return self.cleaned_data.get('password_repeat')


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
