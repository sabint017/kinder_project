# Generated by Django 3.0 on 2019-12-30 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_parents_usertype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_parents',
            old_name='UserType',
            new_name='Usertype',
        ),
    ]
