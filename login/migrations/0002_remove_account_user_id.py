# Generated by Django 2.1.3 on 2018-11-08 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='user_id',
        ),
    ]