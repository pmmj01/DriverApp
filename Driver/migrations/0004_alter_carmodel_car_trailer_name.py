# Generated by Django 4.1.3 on 2022-12-08 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0003_alter_carmodel_car_trailer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='car_trailer_name',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='car_trailer', to='Driver.trailermodel'),
        ),
    ]
