# Generated by Django 5.0.6 on 2024-07-02 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_tg_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='телеграмм chat_id'),
        ),
    ]