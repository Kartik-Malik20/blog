# Generated by Django 5.0.1 on 2024-02-02 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_comments_blog_com'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='blog_com',
            new_name='blog',
        ),
    ]