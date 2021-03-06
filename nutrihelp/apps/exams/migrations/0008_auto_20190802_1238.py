# Generated by Django 2.2.4 on 2019-08-02 17:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20190802_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('upper', models.IntegerField(verbose_name='Puntaje superior')),
                ('bottom', models.IntegerField(verbose_name='Puntaje inferior')),
                ('content', tinymce.models.HTMLField(verbose_name='Contenido')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='answeredquestion',
            options={'ordering': ['-created_at'], 'verbose_name': 'Repuesta a pregunta', 'verbose_name_plural': 'Respuesta a preguntas'},
        ),
    ]
