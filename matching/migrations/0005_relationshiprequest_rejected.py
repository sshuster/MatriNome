# Generated by Django 2.2.6 on 2019-11-05 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0004_auto_20191106_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationshiprequest',
            name='rejected',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]