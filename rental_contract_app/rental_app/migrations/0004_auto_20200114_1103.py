# Generated by Django 3.0 on 2020-01-14 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_app', '0003_auto_20200114_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalimages',
            name='apartment_pictures',
            field=models.ImageField(upload_to='images'),
        ),
    ]
