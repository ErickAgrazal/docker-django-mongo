# Generated by Django 2.2.4 on 2019-08-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_auto_20190802_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='bottom',
            field=models.IntegerField(default=0, verbose_name='% Puntaje inferior'),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='upper',
            field=models.IntegerField(default=100, verbose_name='% Puntaje superior'),
        ),
    ]
