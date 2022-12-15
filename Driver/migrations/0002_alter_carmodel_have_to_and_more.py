# Generated by Django 4.1.3 on 2022-12-14 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='have_to',
            field=models.CharField(choices=[('--', ''), ('B', 'B'), ('B+E', 'B+E'), ('C', 'C'), ('C+E', 'C+E')], max_length=4),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='driving_license',
            field=models.CharField(choices=[('--', ''), ('B', 'B'), ('B+E', 'B+E'), ('C', 'C'), ('C+E', 'C+E')], max_length=5),
        ),
    ]
