# Generated by Django 3.0 on 2020-02-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0031_presentday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='present_days_count',
        ),
    ]
