# Generated by Django 2.2.7 on 2020-02-13 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0035_auto_20200213_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.SID'),
        ),
    ]
