# Generated by Django 5.0.1 on 2024-02-05 06:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_rename_blog_com_comments_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
