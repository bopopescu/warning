# Generated by Django 2.0.5 on 2018-06-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subordinates', '0006_auto_20180618_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='threshold',
            name='multiplication_factor',
            field=models.FloatField(default=1),
        ),
    ]