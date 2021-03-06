# Generated by Django 2.0.1 on 2019-10-31 04:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankomat', '0002_auto_20191031_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='card_number',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999999), django.core.validators.MinValueValidator(1000100010001000)], verbose_name='Card Number'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cvv',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(100)], verbose_name='Cvv'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='password',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1000)], verbose_name='Password'),
        ),
    ]
