# Generated by Django 3.2.25 on 2024-04-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_hotelowner',
            field=models.BooleanField(default=False, verbose_name='Is hotelowner '),
        ),
    ]
