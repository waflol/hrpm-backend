# Generated by Django 3.2.16 on 2022-11-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recruiter', '0001_initial'),
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvcandidate',
            name='applied',
            field=models.ManyToManyField(blank=True, null=True, to='recruiter.Job'),
        ),
    ]
