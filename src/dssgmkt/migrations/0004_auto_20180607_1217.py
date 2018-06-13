# Generated by Django 2.0.6 on 2018-06-07 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dssgmkt', '0003_auto_20180604_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='private_reviewer_notes',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='public_reviewer_comments',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='resolution_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='organizationmembershiprequest',
            name='status',
            field=models.CharField(choices=[('NEW', 'Pending review'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='NEW', max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='available_data',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='available_staff',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='challenges',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='developer_agreement',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='motivation',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_impact',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='scoping_process',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_summary',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='solution_description',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='projectlog',
            name='change_description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='description',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='onboarding_instructions',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='projecttaskreview',
            name='review_result',
            field=models.CharField(choices=[('NEW', 'Pending review'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='NEW', max_length=3),
        ),
        migrations.AlterField(
            model_name='projecttaskreview',
            name='reviewer_comment',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='projecttaskreview',
            name='volunteer_comment',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='private_reviewer_notes',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='public_reviewer_comments',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='status',
            field=models.CharField(choices=[('NEW', 'Pending review'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='NEW', max_length=3),
        ),
        migrations.AlterField(
            model_name='volunteerapplication',
            name='volunteer_application_letter',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='cover_letter',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerprofile',
            name='volunteer_status',
            field=models.CharField(choices=[('NEW', 'Pending review'), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='NEW', max_length=3),
        ),
    ]
