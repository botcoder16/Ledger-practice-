# Generated by Django 4.2.4 on 2023-12-09 19:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0012_alter_transaction_groupid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='usernames',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
