# Generated by Django 5.0.2 on 2024-02-18 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_room_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='session_key',
            field=models.CharField(max_length=1000),
        ),
    ]
