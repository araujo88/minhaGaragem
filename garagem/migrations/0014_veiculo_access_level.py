# Generated by Django 3.2.6 on 2021-08-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0013_remove_veiculo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='access_level',
            field=models.IntegerField(choices=[(0, 'Public'), (1, 'Private')], default=1),
        ),
    ]
