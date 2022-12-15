import random
from Driver.models import *
from Driver.choices import *

from faker import Faker

fake = Faker('en')


def create_fake_user():
    country_calling_code = '+99'
    number = (str.join('', country_calling_code + str(random.randint(100000000, 999999999))))
    phone_number = number
    first_name = fake.first_name()
    last_name = fake.last_name()
    user_type = random.choice(USER)[0]
    driving_license = random.choice(DRIVER_LICENSE)[0]
    password = 'Test123!'
    users = UserModel.objects.create_user(phone_number=phone_number,
                                          first_name=first_name,
                                          last_name=last_name,
                                          user_type=user_type,
                                          driving_license=driving_license,
                                          password=password)
    return users


def random_user():
    user = UserModel.objects.all()
    return random.choice(user)


def create_fake_address_company_from():
    company_name = fake.company()
    address_country = random.choice(COUNTRY)[0]
    address_city = fake.city()
    address_zip_code = fake.postcode()
    address_street = fake.street_name()
    address_property_first = fake.building_number()
    address_property_second = fake.building_number()
    address_more_info = fake.bs()
    address_company = AddressCompanyFromModel.objects.create(company_name=company_name,
                                                             address_country=address_country,
                                                             address_city=address_city,
                                                             address_zip_code=address_zip_code,
                                                             address_street=address_street,
                                                             address_property_first=address_property_first,
                                                             address_property_second=address_property_second,
                                                             address_more_info=address_more_info)
    return address_company


def create_fake_address_company_to():
    company_name = fake.company()
    address_country = random.choice(COUNTRY)[0]
    address_city = fake.city()
    address_zip_code = fake.postcode()
    address_street = fake.street_name()
    address_property_first = fake.building_number()
    address_property_second = fake.building_number()
    address_more_info = fake.bs()
    address_company = AddressCompanyToModel.objects.create(company_name=company_name,
                                                           address_country=address_country,
                                                           address_city=address_city,
                                                           address_zip_code=address_zip_code,
                                                           address_street=address_street,
                                                           address_property_first=address_property_first,
                                                           address_property_second=address_property_second,
                                                           address_more_info=address_more_info)
    return address_company


def create_fake_trailer():
    model = fake.random.choice(TRAILER)[0]
    trailer_number = fake.license_plate()
    weighs = random.randint(3000, 10000)
    tons_can_load = random.randint(2000, 18000)
    cargo_space = random.choice(TRAILER_SPACE)[0]

    trailer = TrailerModel.objects.create(model=model,
                                          trailer_number=trailer_number,
                                          weighs=weighs,
                                          tons_can_load=tons_can_load,
                                          cargo_space=cargo_space)
    return trailer


def create_fake_car():
    model = fake.random.choice(TRUCK)[0]
    have_to = random.choice(DRIVER_LICENSE)[0]
    car_number = fake.license_plate()
    weighs = random.randint(2400, 8700)
    tons_can_load = random.randint(1000, 18000)
    cargo_space = random.choice(TRUCK_SPACE)[0]
    car = CarModel.objects.create(model=model,
                                      have_to=have_to,
                                      car_number=car_number,
                                      weighs=weighs,
                                      tons_can_load=tons_can_load,
                                      cargo_space=cargo_space)
    return car
