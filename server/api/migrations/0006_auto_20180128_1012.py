# Generated by Django 2.0.1 on 2018-01-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0005_auto_20180128_1006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='is_read',
        ),
        migrations.AddField(
            model_name='inbox',
            name='is_read',
            field=models.BooleanField(default=False),
        ),
    ]
