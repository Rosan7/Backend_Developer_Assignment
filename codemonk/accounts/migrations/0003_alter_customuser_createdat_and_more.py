# Generated by Django 5.0.1 on 2024-02-08 18:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_createdat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='createdAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='modifiedAt',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
