# Generated by Django 2.2.7 on 2020-03-11 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0042_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Contacts',
        ),
    ]