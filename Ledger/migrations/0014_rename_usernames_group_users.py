# Generated by Django 4.2.4 on 2023-12-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_group_usernames'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='usernames',
            new_name='users',
        ),
    ]