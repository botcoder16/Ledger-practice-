# Generated by Django 4.2.4 on 2023-12-10 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0017_group_no_of_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reciever_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
