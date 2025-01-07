# Generated by Django 5.1.4 on 2025-01-07 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='meal_type',
            field=models.CharField(choices=[('B', 'صبحانه'), ('L', 'ناهار'), ('D', 'شام')], default='L', max_length=10),
        ),
    ]
