# Generated by Django 5.1.4 on 2025-01-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.FloatField(default=0.0),
        ),
    ]
