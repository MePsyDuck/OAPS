# Generated by Django 2.0.1 on 2018-01-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0004_auto_20180128_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]