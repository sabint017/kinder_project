# Generated by Django 3.0 on 2019-12-30 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191230_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_parents',
            name='Utype',
            field=models.CharField(default='parent', max_length=200),
            preserve_default=False,
        ),
    ]
