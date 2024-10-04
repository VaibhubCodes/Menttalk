# Generated by Django 5.0 on 2024-06-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_delete_timeblock_alter_mentor_time_blocks'),
        ('webadmin', '0002_custompage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.ImageField(upload_to='category_icons/')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='company_logos/')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='call_to_action_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='call_to_action_url',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_image',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='mentor_search_placeholder',
            field=models.CharField(default='Search for a mentor...', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='reviews',
            field=models.ManyToManyField(related_name='homepage_reviews', to='core.review'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='top_mentors',
            field=models.ManyToManyField(related_name='top_mentors', to='core.mentor'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='webadmin.category'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='company_logos',
            field=models.ManyToManyField(related_name='company_logos', to='webadmin.companylogo'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='faqs',
            field=models.ManyToManyField(related_name='homepage_faqs', to='webadmin.faq'),
        ),
    ]
