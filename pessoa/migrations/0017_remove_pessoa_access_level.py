# Generated by Django 3.2.6 on 2021-09-06 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0016_alter_pessoa_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='access_level',
        ),
    ]
