# Generated by Django 5.0.1 on 2024-02-02 05:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_blog_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blogcat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myblog.category'),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='like_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='blog_post',
            name='view_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
