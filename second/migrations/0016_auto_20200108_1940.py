# Generated by Django 2.2.7 on 2020-01-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0015_auto_20200108_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='day',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='remarks',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
