# Generated by Django 2.2.4 on 2019-08-02 18:06

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_auto_20190802_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommendation',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
