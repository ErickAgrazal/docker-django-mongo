# Generated by Django 2.2.4 on 2019-08-02 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0009_auto_20190802_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recommendation',
            options={'ordering': ['-created_at'], 'verbose_name': 'Recomendación', 'verbose_name_plural': 'Recomendaciones'},
        ),
        migrations.AddField(
            model_name='answer',
            name='weight',
            field=models.IntegerField(default=10, verbose_name='Puntaje'),
        ),
    ]
