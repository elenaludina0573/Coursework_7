# Generated by Django 5.0.6 on 2024-07-08 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='is_good',
            field=models.BooleanField(choices=[(True, 'Приятная'), (False, 'Нет')], default=True, verbose_name='Приятная'),
        ),
    ]