# Generated by Django 4.2.4 on 2023-12-02 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_transaction_alter_choice_question_delete_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]