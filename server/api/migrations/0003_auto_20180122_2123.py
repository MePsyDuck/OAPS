# Generated by Django 2.0.1 on 2018-01-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('api', '0002_auto_20180121_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='acc_type',
            field=models.IntegerField(choices=[(1, 'Student'), (2, 'Faculty')], default=1),
        ),
    ]
