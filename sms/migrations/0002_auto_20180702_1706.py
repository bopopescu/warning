# Generated by Django 2.0 on 2018-07-02 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='provider',
            name='secure_hash',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
