# Generated by Django 3.2.8 on 2021-11-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_alter_teachers_options'),
        ('klients', '0004_alter_statusklienta_status'),
        ('tasks', '0002_auto_20211109_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='teachers.teachers', verbose_name='Ответственный'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='klient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='klients.klients', verbose_name='Клиент'),
        ),
    ]
