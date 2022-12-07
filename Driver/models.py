from django.db import models
# from django.db.models import Model
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin, Permission, AbstractUser, AbstractBaseUser, User, \
    BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

# from .managers import CustomUserManager


USER = (
    ('admin', 'Admin'),
    ('manager', 'Manager'),
    ('personnel', 'Personnel'),
    ('dispatcher', 'Dispatcher'),
    ('forwarder', 'Forwarder'),
    ('driver', 'Driver'),
)

STATUS = (
    (1, "Positive"),
)

STATUS_PROBLEM = (
    (1, "Positive"),
    (2, "Raport problem")
)

NUMBER = (
    ("PL", "+48"),
    ("DE", "+49"),
    ("I", "+39"),
)

DRIVER_LICENSE = (
    (1, "B"),
    (2, "B+E"),
    (3, "C"),
    (4, "C+E"),
)

COUNTRY = (
    (1, "Albania"),
    (2, "Andorra"),
    (3, "Austria"),
    (4, "Belarus"),
    (5, "Belgium"),
    (6, "Bosnia and Herzegovina"),
    (7, "Bulgaria"),
    (8, "Croatia"),
    (9, "Cyprus"),
    (10, "Czech Republic"),
    (11, "Denmark"),
    (12, "Estonia"),
    (13, "Finland"),
    (14, "France"),
    (15, "Germany"),
    (16, "United Kingdom"),
    (17, "Greece"),
    (18, "Hungary"),
    (19, "Iceland"),
    (20, "Ireland"),
    (21, "Italy"),
    (22, "Latvia"),
    (23, "Liechtenstein"),
    (24, "Lithuania"),
    (25, "Luxembourg"),
    (26, "Macedonia"),
    (27, "Malta"),
    (28, "Moldova"),
    (29, "Monaco"),
    (30, "Montenegro"),
    (31, "Netherlands"),
    (32, "Norway"),
    (33, "Poland"),
    (34, "Portugal"),
    (35, "Romania"),
    (36, "Russia"),
    (37, "San Marino"),
    (38, "Serbia"),
    (39, "Slovakia"),
    (40, "Slovenia"),
    (41, "Spain"),
    (42, "Sweden"),
    (43, "Switzerland"),
    (44, "Turkey"),
    (45, "Ukraine"),
    (46, "Vatican"),
)

TRUCK = (
    (1, "Bus"),
    (2, "Bus Trailer"),
    (3, "Small Truck"),
    (4, "Solo"),
    (5, "Truck Tandem"),
    (6, "Truck Trailer"),
)

TRUCK_SPACE = (
    (1, 'Truck'),
    (2, '8 ep'),
    (3, '9 ep'),
    (4, '10 ep'),
    (5, '12 ep'),
    (6, '18 ep'),
    (7, '19 ep'),

)

TRAILER = (
    (1, 'Tilt Trailer'),
    (2, 'Refrigerator Trailer'),
    (3, 'Container Trailer'),
    (4, 'Trailer Floor'),
    (5, 'Trailer Moving floor'),
    (6, 'Special Trailer'),
    (7, 'Isothermal Trailer'),
    (8, 'Tank Trailer'),
)

TRAILER_SPACE = (
    (1, '8 ep'),
    (2, '9 ep'),
    (3, '10 ep'),
    (4, '12 ep'),
    (5, '18 ep'),
    (6, '19 ep'),
    (7, '20 ep'),
    (8, '32 ep'),
    (9, '33 ep'),
    (10, '36 ep'),
)

FIX = (
    (1, 'FIX'),
    (2, ''),
)

CUSTOMS_CLEARANCE = (
    (1, 'CUSTOMS'),
    (2, '')
)


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
    company_name = models.CharField(max_length=100, blank=False)
    address_country = models.PositiveSmallIntegerField(choices=COUNTRY, blank=False)
    address_city = models.CharField(max_length=64, blank=False)
    address_zip_code = models.CharField(max_length=5, blank=False)
    address_street = models.CharField(max_length=128, blank=False)
    address_property_first = models.CharField(max_length=8, blank=False)
    address_property_second = models.CharField(max_length=8, blank=True)
    address_more_info = models.TextField(blank=True)

    def __str__(self):
        return (f"{self.company_name} - {self.address_city} ({self.address_country})")


class AddressCompanyToModel(models.Model):
    company_name = models.CharField(max_length=100, blank=False)
    address_country = models.PositiveSmallIntegerField(choices=COUNTRY, blank=False)
    address_city = models.CharField(max_length=64, blank=False)
    address_zip_code = models.CharField(max_length=5, blank=False)
    address_street = models.CharField(max_length=128, blank=False)
    address_property_first = models.CharField(max_length=8, blank=False)
    address_property_second = models.CharField(max_length=8, blank=True)
    address_more_info = models.TextField(blank=True)

    def __str__(self):
        return (f"{self.company_name} - {self.address_city} ({self.address_country})")


class DriverModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    driver_license = models.PositiveSmallIntegerField(choices=DRIVER_LICENSE, blank=False)

    @property
    def fullname(self):
        return (f"{self.user.first_name} {self.user.last_name}")

    def __str__(self):
        return (
            f"{self.user.phone_number(0)} {self.user.phone_number(1)} {self.user.phone_number(2)} - {self.fullname} ({self.user.user_type})")


class ForwarderModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    @property
    def fullname(self):
        return (f"{self.user.first_name} {self.user.last_name}")

    def __str__(self):
        return (
            f"{self.user.phone_number(0)} {self.user.phone_number(1)} {self.user.phone_number(2)} - {self.fullname} ({self.user.user_type})")


class TrailerModel(models.Model):
    model = models.CharField(max_length=30, choices=TRAILER, blank=False)
    trailer_number = models.CharField(max_length=8, blank=False, primary_key=True)
    weighs = models.PositiveSmallIntegerField(default=0, blank=False)
    tons_can_load = models.PositiveSmallIntegerField(default=0, blank=False)
    cargo_space = models.CharField(max_length=6, choices=TRAILER_SPACE)

    def __str__(self):
        return (f"{self.model} - {self.trailer_number} ({self.tons_can_load}/{self.cargo_space})")


class CarModel(models.Model):
    model = models.CharField(max_length=20, choices=TRUCK, blank=False)
    have_to = models.CharField(max_length=4, choices=DRIVER_LICENSE, blank=False)
    car_number = models.CharField(max_length=8, blank=False, primary_key=True)
    weighs = models.PositiveSmallIntegerField(default=0, blank=False)
    tons_can_load = models.PositiveSmallIntegerField(default=0)
    cargo_space = models.CharField(max_length=5, choices=TRUCK_SPACE)
    trailer = models.OneToOneField(TrailerModel, on_delete=models.CASCADE, related_name="car_trailer", blank=True)

    def __str__(self):
        return (f"{self.model} - {self.trailer_number} ({self.tons_can_load}/{self.cargo_space})")


class CargoModel(models.Model):
    company_address_from = models.ForeignKey(AddressCompanyFromModel, on_delete=models.CASCADE,
                                             related_name="cargo_company_address_from")
    loading_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    loading_hour = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    company_address_to = models.ForeignKey(AddressCompanyToModel, on_delete=models.CASCADE,
                                           related_name="cargo_company_address_to")
    unloading_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
    unloading_hour = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    description = models.TextField()
    fix = models.CharField(max_length=3, choices=FIX)
    customs = models.CharField(max_length=7, choices=CUSTOMS_CLEARANCE)
    weight = models.PositiveSmallIntegerField(default=0)
    pallets = models.PositiveSmallIntegerField(default=0)
    place_of_pallets = models.PositiveSmallIntegerField(default=0)
    truck = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="cargo_truck")
    forwarder = models.ForeignKey(ForwarderModel, on_delete=models.CASCADE, related_name="cargo_forwarder")
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False)

    def __str__(self):
        return (f"{self.pk} - {self.company_address_from} > {self.company_address_to} ({self.customs}/{self.fix})")


class PlanCargoModel(models.Model):
    driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE, related_name="plan_cargo_driver")
    truck = models.OneToOneField(CarModel, on_delete=models.CASCADE, related_name="plan_cargo_truck")
    forwarder = models.ForeignKey(ForwarderModel, on_delete=models.CASCADE, related_name="plan_cargo_forwarder")
    description = models.ForeignKey(CargoModel, on_delete=models.CASCADE, related_name="plan_cargo_description")
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False)

    def __str__(self):
        return (f"{self.driver} - {self.truck} ({self.forwarder})")


class DriverWorkerModel(models.Model):
    point = models.ForeignKey(PlanCargoModel, on_delete=models.CASCADE, related_name="driver_worker_point")
    date = models.DateField(auto_now=False, auto_now_add=True, blank=False)
    confirm_arrival = models.CharField(max_length=32, choices=STATUS)
    confirm_unloading = models.CharField(max_length=32, choices=STATUS)
    confirm_loading = models.CharField(max_length=32, choices=STATUS)
    raport = models.CharField(max_length=32, choices=STATUS_PROBLEM)
    message_to = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="driver_worker_message_to")
    message = models.TextField()

    def __str__(self):
        return (f"{self.pk} - {self.point}")


class MessageModel(models.Model):
    message_to = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="message_message_to")
    message = models.TextField()
