# Generated by Django 2.1.2 on 2018-11-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg2db', '0004_auto_20181107_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addOnMsg',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='companyName',
            field=models.CharField(default='', max_length=100),
        ),
    ]