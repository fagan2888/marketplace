# Generated by Django 2.0.6 on 2018-07-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssgmkt', '0024_auto_20180711_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectlog',
            name='change_target',
            field=models.CharField(blank=True, choices=[('TK', 'Task'), ('VA', 'Volunteer application'), ('ST', 'Staff'), ('TK', 'Task review'), ('VO', 'Volunteer'), ('VO', 'Status'), ('VO', 'Information')], default='TK', max_length=2, null=True),
        ),
    ]
