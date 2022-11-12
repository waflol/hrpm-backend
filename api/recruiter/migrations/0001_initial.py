# Generated by Django 3.2.16 on 2022-11-12 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('established', models.DateField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('experience_required', models.PositiveIntegerField(default=0)),
                ('num_candidate_need', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('postition', models.CharField(max_length=255)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField()),
                ('salary', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('status', models.PositiveIntegerField(default=0)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiter.company')),
                ('job_types', models.ManyToManyField(blank=True, to='tag.JobTag')),
                ('programming_language_tags', models.ManyToManyField(blank=True, to='tag.ProgrammingLanguageTag')),
            ],
        ),
    ]
