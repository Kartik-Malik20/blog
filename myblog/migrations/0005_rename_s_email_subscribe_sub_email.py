# Generated by Django 5.0.1 on 2024-01-16 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_subscribe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='s_email',
            new_name='sub_email',
        ),
    ]
