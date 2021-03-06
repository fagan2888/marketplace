# Generated by Django 2.0.6 on 2018-06-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_auto_20180623_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='request_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Date and time in which the membership request was created', verbose_name='Review date'),
        ),
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='resolution_date',
            field=models.DateTimeField(auto_now=True, help_text='Date and time in which the membership request was resolved', null=True, verbose_name='Resolution date'),
        ),
    ]
