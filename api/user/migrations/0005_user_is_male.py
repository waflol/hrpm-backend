# Generated by Django 3.2.16 on 2022-11-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20221111_0317'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_male',
            field=models.BooleanField(default=False),
        ),
    ]
