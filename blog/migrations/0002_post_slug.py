# Generated by Django 4.1.3 on 2022-11-17 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]