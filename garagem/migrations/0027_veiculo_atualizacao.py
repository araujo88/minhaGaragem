# Generated by Django 3.2.6 on 2021-09-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0026_veiculo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
