# Generated by Django 2.2.7 on 2020-01-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0010_remove_food_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='full_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
