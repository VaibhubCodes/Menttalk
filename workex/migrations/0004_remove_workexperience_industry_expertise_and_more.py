# Generated by Django 5.0 on 2024-06-19 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('industry', '0001_initial'),
        ('workex', '0003_alter_workexperience_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='industry_expertise',
        ),
        migrations.AddField(
            model_name='workexperience',
            name='industry_expertise',
            field=models.ManyToManyField(related_name='work_experiences', to='industry.expertise'),
        ),
    ]
