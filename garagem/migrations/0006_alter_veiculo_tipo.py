# Generated by Django 3.2.6 on 2021-08-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_alter_veiculo_ano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='tipo',
            field=models.CharField(choices=[('Carro', 'Carro'), ('Moto', 'Moto')], max_length=5),
        ),
    ]