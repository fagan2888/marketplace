# Generated by Django 2.0.6 on 2018-07-10 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0021_auto_20180710_1109'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='projecttaskrequirement',
            unique_together={('skill', 'task')},
        ),
    ]