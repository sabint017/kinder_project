# Generated by Django 2.2.7 on 2020-01-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200112_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_parents',
            name='ChildGrade',
            field=models.CharField(max_length=20),
        ),
    ]
