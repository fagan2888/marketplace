# Generated by Django 2.0.6 on 2018-07-18 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0034_volunteerapplication_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='reviewer',
            field=models.ForeignKey(blank=True, help_text='User that reviewed the membership application', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_organization_membership_request', to=settings.AUTH_USER_MODEL, verbose_name='Review author'),
        ),
        migrations.AlterField(
            model_name='projecttaskreview',
            name='reviewer',
            field=models.ForeignKey(blank=True, help_text='The user that did the QA review of this task.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_project_task', to=settings.AUTH_USER_MODEL, verbose_name='Review author'),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='reviewer',
            field=models.ForeignKey(blank=True, help_text='The user that did the review of this volunteer application.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewed_volunteer_application', to=settings.AUTH_USER_MODEL, verbose_name='Review author'),
        ),
    ]