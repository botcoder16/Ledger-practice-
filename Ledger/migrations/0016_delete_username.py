# Generated by Django 4.2.4 on 2023-12-09 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_alter_transaction_groupid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Username',
        ),
    ]