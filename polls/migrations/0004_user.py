# Generated by Django 4.2.4 on 2023-12-03 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_transaction_time_delete_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_phone', models.CharField(max_length=12)),
                ('Money_sent', models.IntegerField()),
                ('Money_recieved', models.IntegerField()),
            ],
        ),
    ]
