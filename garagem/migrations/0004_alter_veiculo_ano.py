# Generated by Django 3.2.6 on 2021-08-16 04:40

import django.core.validators
from django.db import migrations, models
import garagem.models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_alter_veiculo_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='ano',
            field=models.PositiveIntegerField(default=2021, validators=[django.core.validators.MinValueValidator(1984), garagem.models.max_value_current_year]),
        ),
    ]
