# Generated by Django 2.2.6 on 2019-11-05 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='from_user',
            new_name='current_user',
        ),
        migrations.RenameField(
            model_name='partner',
            old_name='to_user',
            new_name='its_partner',
        ),
    ]
