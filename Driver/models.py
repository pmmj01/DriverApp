from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin, Permission, AbstractUser, AbstractBaseUser, User, \
    BaseUserManager
from .choices import *


class CustomUserManager(BaseUserManager):
    def _create_user(self, phone_number, user_type, first_name, last_name, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The given phone number must be set')
        if not user_type:
            raise ValueError('The given user type must be set')
        if not first_name:
            raise ValueError('The given first name must be set')
        if not last_name:
            raise ValueError('The given last name must be set')
        user = self.model(phone_number=phone_number, user_type=user_type, first_name=first_name, last_name=last_name,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, user_type, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone_number, user_type, first_name, last_name, password, **extra_fields)

    def create_superuser(self, phone_number, user_type, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone_number, user_type, first_name, last_name, password, **extra_fields)


class UserModel(AbstractUser):
    username = None
    phone_regex = RegexValidator(regex=r'^(\+)(\d{2,3})(\d{9,11})$',
                                 message='Phone number must be entered in the format: "+00000000000". Up to 14 digits allowed.')
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, unique=True)
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    user_type = models.CharField(max_length=20, choices=USER)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['user_type', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.full_name()} : {self.phone_number} ({self.user_type.title()})'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class AddressCompanyFromModel(models.Model):
    company_name = models.CharField(max_length=100, blank=False, name='company_name')
    address_country = models.CharField(max_length=15, choices=COUNTRY, blank=False, name='address_country')
    address_city = models.CharField(max_length=64, blank=False, name='address_city')
    address_zip_code = models.CharField(max_length=5, blank=False, name='address_zip_code')
    address_street = models.CharField(max_length=128, blank=False, name='address_street')
    address_property_first = models.CharField(max_length=8, blank=False, name='address_property_first')
    address_property_second = models.CharField(max_length=8, blank=True, name='address_property_second')
    address_more_info = models.TextField(blank=True, name='address_more_info')

    def __str__(self):
        return f'{self.company_name} - {self.address_city} ({self.country()})'

    def country(self):
        return self.address_country


class AddressCompanyToModel(models.Model):
    company_name = models.CharField(max_length=100, blank=False, name='company_name')
    address_country = models.CharField(max_length=15, choices=COUNTRY, blank=False, name='address_country')
    address_city = models.CharField(max_length=64, blank=False, name='address_city')
    address_zip_code = models.CharField(max_length=5, blank=False, name='address_zip_code')
    address_street = models.CharField(max_length=128, blank=False, name='address_street')
    address_property_first = models.CharField(max_length=8, blank=False, name='address_property_first')
    address_property_second = models.CharField(max_length=8, blank=True, name='address_property_second')
    address_more_info = models.TextField(blank=True, name='address_more_info')

    def __str__(self):
        return f'{self.company_name} - {self.address_city} ({self.address_country})'


class DriverModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, name='worker')
    driver_license = models.CharField(max_length=4, choices=DRIVER_LICENSE, blank=False, name='driver_license')

    @property
    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.full_name()} : {self.user.phone_number} ({self.user.user_type.title()}) {self.driver_license}'


class ForwarderModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, name='worker')

    @property
    def fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return f'{self.user.full_name()} : {self.user.phone_number} ({self.user.user_type.title()})'


class TrailerModel(models.Model):
    model = models.CharField(max_length=30, choices=TRAILER, blank=False, name='model')
    trailer_number = models.CharField(max_length=9, blank=False, unique=True, name='trailer_number')
    weighs = models.PositiveSmallIntegerField(default=0, blank=False, name='weighs')
    tons_can_load = models.PositiveSmallIntegerField(default=0, blank=False, name='tons_can_load')
    cargo_space = models.CharField(max_length=15, choices=TRAILER_SPACE, name='cargo_space')

    def __str__(self):
        return f'{self.pk}# {self.model} - {self.trailer_number} ({self.tons_can_load}/{self.cargo_space})'


class CarModel(models.Model):
    model = models.CharField(max_length=20, choices=TRUCK, blank=False, name='model')
    have_to = models.CharField(max_length=4, choices=DRIVER_LICENSE, blank=False, name='have_to')
    car_number = models.CharField(max_length=9, blank=False, unique=True, name='car_number')
    weighs = models.PositiveSmallIntegerField(default=0, blank=False, name='weighs')
    tons_can_load = models.PositiveSmallIntegerField(default=0, name='tons_can_load')
    cargo_space = models.CharField(max_length=15, choices=TRUCK_SPACE, name='cargo_space')
    trailer = models.OneToOneField(TrailerModel, on_delete=models.CASCADE, blank=True, null=True, related_name="car_trailer", name='trailer')

    def __str__(self):
        return f'{self.model} - {self.trailer.trailer_number} ({self.tons_can_load}/{self.cargo_space})'


class CargoModel(models.Model):
    company_address_from = models.ForeignKey(AddressCompanyFromModel, on_delete=models.CASCADE,
                                             related_name='cargo_company_address_from', name='company_address_from')
    loading_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    loading_hour = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    company_address_to = models.ForeignKey(AddressCompanyToModel, on_delete=models.CASCADE,
                                           related_name='cargo_company_address_to', name='company_address_to')
    unloading_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    unloading_hour = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    description = models.TextField()
    notification = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    reference_number = models.CharField(max_length=20)
    fix = models.CharField(max_length=3, choices=FIX)
    customs = models.CharField(max_length=7, choices=CUSTOMS_CLEARANCE)
    weight = models.PositiveSmallIntegerField(default=0, name='weighs')
    pallets = models.PositiveSmallIntegerField(default=0, name='pallets')
    place_of_pallets = models.PositiveSmallIntegerField(default=0, name='place_of_pallets')
    truck = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cargo_truck")
    forwarder = models.ForeignKey(ForwarderModel, on_delete=models.CASCADE, related_name="cargo_forwarder")
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.pk} - {self.company_address_from} > {self.company_address_to} ({self.customs}/{self.fix})'


class PlanCargoModel(models.Model):
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE, related_name='plan_cargo_driver')
    truck = models.OneToOneField(CarModel, on_delete=models.CASCADE, related_name='plan_cargo_truck')
    forwarder = models.ForeignKey(ForwarderModel, on_delete=models.CASCADE, related_name='plan_cargo_forwarder')
    description = models.ForeignKey(CargoModel, on_delete=models.CASCADE, related_name='plan_cargo_description')
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False)

    def __str__(self):
        return f'{self.driver} - {self.truck} ({self.forwarder})'


class DriverWorkerModel(models.Model):
    point = models.ForeignKey(PlanCargoModel, on_delete=models.CASCADE, related_name='driver_worker_point')
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False, name='date')
    confirm_arrival = models.CharField(max_length=32, choices=STATUS, name='confirm_arrival')
    confirm_unloading = models.CharField(max_length=32, choices=STATUS, name='confirm_unloading')
    confirm_loading = models.CharField(max_length=32, choices=STATUS, name='confirm_loading')
    raport = models.CharField(max_length=32, choices=STATUS_PROBLEM, name='raport')
    message_to = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='driver_worker_message_to')
    message = models.TextField()

    def __str__(self):
        return f'{self.pk} - {self.point}'


class MessageModel(models.Model):
    message_to = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='message_message_to')
    message = models.TextField()
