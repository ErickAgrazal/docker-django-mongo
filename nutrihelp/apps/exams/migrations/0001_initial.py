# Generated by Django 2.2.4 on 2019-08-02 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Pregunta')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('title', models.CharField(blank=True, max_length=20, null=True, verbose_name='Respuesta')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to='exams.Question', verbose_name='Pregunta')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
