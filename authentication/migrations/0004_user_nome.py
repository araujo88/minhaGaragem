# Generated by Django 3.2.6 on 2021-08-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20210816_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nome',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
