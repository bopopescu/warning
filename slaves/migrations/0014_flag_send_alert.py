# Generated by Django 2.0.5 on 2018-09-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subordinates', '0013_auto_20180703_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='send_alert',
            field=models.BooleanField(default=False),
        ),
    ]
