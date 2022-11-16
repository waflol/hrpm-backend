# Generated by Django 3.2.16 on 2022-11-16 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0003_job_job_types'),
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worklow', to='recruiter.job'),
        ),
    ]
