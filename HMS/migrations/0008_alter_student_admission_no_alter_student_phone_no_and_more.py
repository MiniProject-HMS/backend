# Generated by Django 4.0.5 on 2022-06-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HMS', '0007_workers_complaints_hostel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='admission_no',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_no',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_no',
            field=models.BigIntegerField(default=0),
        ),
    ]