# Generated by Django 4.2.5 on 2023-09-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0007_alter_wpcomment_author_avatar_urls_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpmedia',
            name='slug',
            field=models.SlugField(max_length=500),
        ),
    ]
