# Generated by Django 2.1.2 on 2018-11-09 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msg2db', '0007_remove_note_openid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='companyName',
        ),
    ]
