# Generated by Django 4.1.1 on 2022-11-21 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to='blog/images'),
            preserve_default=False,
        ),
    ]