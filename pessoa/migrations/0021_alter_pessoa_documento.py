# Generated by Django 3.2.6 on 2021-09-06 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0020_pessoa_documento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='documento',
            field=models.CharField(max_length=20),
        ),
    ]