# Generated by Django 2.0.6 on 2018-07-18 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dssgmkt', '0030_auto_20180713_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectDiscussionChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Descriptive name that identifies the discussion channel within the project.', max_length=100, verbose_name='Name')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dssgmkt.Project')),
            ],
        ),
        migrations.RemoveField(
            model_name='projectcomment',
            name='project',
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dssgmkt.ProjectDiscussionChannel'),
            preserve_default=False,
        ),
    ]
