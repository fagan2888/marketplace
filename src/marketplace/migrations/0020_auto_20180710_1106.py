# Generated by Django 2.0.6 on 2018-07-10 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0019_auto_20180705_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttaskreview',
            name='volunteer',
            field=models.ForeignKey(default=1, help_text='The user requesting a review of this task.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Volunteer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectlog',
            name='change_target',
            field=models.CharField(blank=True, choices=[('TK', 'Task'), ('VA', 'Volunteer application'), ('ST', 'Staff'), ('TK', 'Task review')], default='TK', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='projectlog',
            name='change_type',
            field=models.CharField(blank=True, choices=[('AD', 'Added'), ('RM', 'Removed'), ('ED', 'Edited'), ('FN', 'Completed')], default='AD', max_length=2, null=True),
        ),
    ]