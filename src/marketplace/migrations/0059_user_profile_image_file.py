# Generated by Django 2.0.6 on 2018-07-24 16:58

from django.db import migrations, models
import marketplace.models.common


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0058_project_banner_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_image_file',
            field=models.ImageField(blank=True, help_text='Your profile image.', null=True, upload_to='userprofiles/', validators=[marketplace.models.common.validate_image_size], verbose_name='Profile image'),
        ),
    ]
