# Generated by Django 2.0.8 on 2018-12-01 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subordinates', '0014_flag_send_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='has_icon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='flag',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='flag',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
