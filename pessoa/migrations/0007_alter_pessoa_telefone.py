# Generated by Django 3.2.6 on 2021-08-16 17:55

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0006_auto_20210816_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]