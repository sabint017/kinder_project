# Generated by Django 3.0.2 on 2020-02-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second', '0025_auto_20200210_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='subject1',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='result',
            name='subject2',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='result',
            name='subject3',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='result',
            name='subject4',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
