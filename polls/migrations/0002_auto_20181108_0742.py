# Generated by Django 2.1.3 on 2018-11-08 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Quession',
            new_name='Question',
        ),
    ]
