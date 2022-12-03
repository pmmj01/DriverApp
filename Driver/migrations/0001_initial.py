# Generated by Django 4.1.3 on 2022-12-03 15:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCompanyFromModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address_country', models.PositiveSmallIntegerField(choices=[(1, 'Albania'), (2, 'Andorra'), (3, 'Austria'), (4, 'Belarus'), (5, 'Belgium'), (6, 'Bosnia and Herzegovina'), (7, 'Bulgaria'), (8, 'Croatia'), (9, 'Cyprus'), (10, 'Czech Republic'), (11, 'Denmark'), (12, 'Estonia'), (13, 'Finland'), (14, 'France'), (15, 'Germany'), (16, 'United Kingdom'), (17, 'Greece'), (18, 'Hungary'), (19, 'Iceland'), (20, 'Ireland'), (21, 'Italy'), (22, 'Latvia'), (23, 'Liechtenstein'), (24, 'Lithuania'), (25, 'Luxembourg'), (26, 'Macedonia'), (27, 'Malta'), (28, 'Moldova'), (29, 'Monaco'), (30, 'Montenegro'), (31, 'Netherlands'), (32, 'Norway'), (33, 'Poland'), (34, 'Portugal'), (35, 'Romania'), (36, 'Russia'), (37, 'San Marino'), (38, 'Serbia'), (39, 'Slovakia'), (40, 'Slovenia'), (41, 'Spain'), (42, 'Sweden'), (43, 'Switzerland'), (44, 'Turkey'), (45, 'Ukraine'), (46, 'Vatican')])),
                ('address_city', models.CharField(max_length=64)),
                ('address_zip_code', models.CharField(max_length=5)),
                ('address_street', models.CharField(max_length=128)),
                ('address_property_first', models.CharField(max_length=8)),
                ('address_property_second', models.CharField(max_length=8)),
                ('address_more_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AddressCompanyToModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('address_country', models.PositiveSmallIntegerField(choices=[(1, 'Albania'), (2, 'Andorra'), (3, 'Austria'), (4, 'Belarus'), (5, 'Belgium'), (6, 'Bosnia and Herzegovina'), (7, 'Bulgaria'), (8, 'Croatia'), (9, 'Cyprus'), (10, 'Czech Republic'), (11, 'Denmark'), (12, 'Estonia'), (13, 'Finland'), (14, 'France'), (15, 'Germany'), (16, 'United Kingdom'), (17, 'Greece'), (18, 'Hungary'), (19, 'Iceland'), (20, 'Ireland'), (21, 'Italy'), (22, 'Latvia'), (23, 'Liechtenstein'), (24, 'Lithuania'), (25, 'Luxembourg'), (26, 'Macedonia'), (27, 'Malta'), (28, 'Moldova'), (29, 'Monaco'), (30, 'Montenegro'), (31, 'Netherlands'), (32, 'Norway'), (33, 'Poland'), (34, 'Portugal'), (35, 'Romania'), (36, 'Russia'), (37, 'San Marino'), (38, 'Serbia'), (39, 'Slovakia'), (40, 'Slovenia'), (41, 'Spain'), (42, 'Sweden'), (43, 'Switzerland'), (44, 'Turkey'), (45, 'Ukraine'), (46, 'Vatican')])),
                ('address_city', models.CharField(max_length=64)),
                ('address_zip_code', models.CharField(max_length=5)),
                ('address_street', models.CharField(max_length=128)),
                ('address_property_first', models.CharField(max_length=8)),
                ('address_property_second', models.CharField(max_length=8)),
                ('address_more_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CargoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loading_date', models.DateField()),
                ('loading_hour', models.DateTimeField()),
                ('unloading_date', models.DateField()),
                ('unloading_hour', models.DateTimeField()),
                ('description', models.TextField()),
                ('fix', models.CharField(choices=[(1, 'FIX'), (2, '')], max_length=3)),
                ('customs', models.CharField(choices=[(1, 'CUSTOMS'), (2, '')], max_length=7)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('pallets', models.PositiveSmallIntegerField(default=0)),
                ('place_of_pallets', models.PositiveSmallIntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('company_address_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_company_address_from', to='Driver.addresscompanyfrommodel')),
                ('company_address_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_company_address_to', to='Driver.addresscompanytomodel')),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('model', models.CharField(choices=[(1, 'Bus'), (2, 'Bus Trailer'), (3, 'Small Truck'), (4, 'Solo'), (5, 'Truck Tandem'), (6, 'Truck Trailer')], max_length=20)),
                ('have_to', models.CharField(choices=[(1, 'B'), (2, 'B+E'), (3, 'C'), (4, 'C+E')], max_length=4)),
                ('car_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('weighs', models.PositiveSmallIntegerField(default=0)),
                ('tons_can_load', models.PositiveSmallIntegerField(default=0)),
                ('cargo_space', models.CharField(choices=[(1, 'Truck'), (2, '8 ep'), (3, '9 ep'), (4, '10 ep'), (5, '12 ep'), (6, '18 ep'), (7, '19 ep')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=128)),
                ('driver_license', models.PositiveSmallIntegerField(choices=[(1, 'B'), (2, 'B+E'), (3, 'C'), (4, 'C+E')])),
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "+00 000000000". Up to 14 digits allowed.', regex='^(\\+)(\\d{2,3})(\\d{9,11})$')])),
            ],
        ),
        migrations.CreateModel(
            name='ForwarderModel',
            fields=[
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=128)),
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "+00000000000". Up to 14 digits allowed.', regex='^(\\+)(\\d{2,3})(\\d{9,11})$')])),
            ],
        ),
        migrations.CreateModel(
            name='TrailerModel',
            fields=[
                ('model', models.CharField(choices=[(1, 'Tilt Trailer'), (2, 'Refrigerator Trailer'), (3, 'Container Trailer'), (4, 'Trailer Floor'), (5, 'Trailer Moving floor'), (6, 'Special Trailer'), (7, 'Isothermal Trailer'), (8, 'Tank Trailer')], max_length=30)),
                ('trailer_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('weighs', models.PositiveSmallIntegerField(default=0)),
                ('tons_can_load', models.PositiveSmallIntegerField(default=0)),
                ('cargo_space', models.CharField(choices=[(1, '8 ep'), (2, '9 ep'), (3, '10 ep'), (4, '12 ep'), (5, '18 ep'), (6, '19 ep'), (7, '20 ep'), (8, '32 ep'), (9, '33 ep'), (10, '36 ep')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('phone_number', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: "+00000000000". Up to 14 digits allowed.', regex='^(\\+)(\\d{2,3})(\\d{9,11})$')])),
                ('user_type', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('personnel', 'Personnel'), ('dispatcher', 'Dispatcher'), ('forwarder', 'Forwarder'), ('driver', 'Driver')], max_length=20)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PlanCargoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_cargo_description', to='Driver.cargomodel')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_cargo_driver', to='Driver.drivermodel')),
                ('forwarder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_cargo_forwarder', to='Driver.forwardermodel')),
                ('truck', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plan_cargo_truck', to='Driver.carmodel')),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_message_to', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverWorkerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('confirm_arrival', models.CharField(choices=[(1, 'Positive')], max_length=32)),
                ('confirm_unloading', models.CharField(choices=[(1, 'Positive')], max_length=32)),
                ('confirm_loading', models.CharField(choices=[(1, 'Positive')], max_length=32)),
                ('raport', models.CharField(choices=[(1, 'Positive'), (2, 'Raport problem')], max_length=32)),
                ('message', models.TextField()),
                ('message_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_worker_message_to', to=settings.AUTH_USER_MODEL)),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='driver_worker_point', to='Driver.plancargomodel')),
            ],
        ),
        migrations.AddField(
            model_name='carmodel',
            name='trailer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='car_trailer', to='Driver.trailermodel'),
        ),
        migrations.AddField(
            model_name='cargomodel',
            name='forwarder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_forwarder', to='Driver.forwardermodel'),
        ),
        migrations.AddField(
            model_name='cargomodel',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_truck', to='Driver.carmodel'),
        ),
    ]
