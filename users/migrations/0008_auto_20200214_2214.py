# Generated by Django 2.2.7 on 2020-02-14 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200211_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_parents',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.School'),
        ),
        migrations.AlterField(
            model_name='user_teachers',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='second.School'),
        ),
    ]