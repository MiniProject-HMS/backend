# Generated by Django 4.0.5 on 2022-06-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('admission_no', models.IntegerField(primary_key=True, serialize=False)),
                ('hostel', models.CharField(default='null', max_length=50)),
                ('room_no', models.IntegerField(default=0)),
                ('password', models.CharField(default='lbscek123', max_length=16)),
            ],
        ),
    ]
