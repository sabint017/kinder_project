# Generated by Django 2.2.7 on 2020-03-09 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('second', '0039_school_schcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='ROUTINES',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30)),
                ('ten_ten45', models.CharField(max_length=30)),
                ('ten45_eleven30', models.CharField(max_length=30)),
                ('eleven45_twelve30', models.CharField(max_length=30)),
                ('twelve30_one15', models.CharField(max_length=30)),
                ('two_two45', models.CharField(max_length=30)),
                ('two45_three30', models.CharField(max_length=30)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=30, null=True)),
                ('food', models.CharField(max_length=30, null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
