# Generated by Django 3.1.2 on 2020-10-08 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_group_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]
