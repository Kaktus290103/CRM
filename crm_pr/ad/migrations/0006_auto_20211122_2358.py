# Generated by Django 3.2.8 on 2021-11-22 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0005_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='thema',
            field=models.TextField(max_length=20, null=True, verbose_name='Тема'),
        ),
        migrations.AlterField(
            model_name='text',
            name='text',
            field=models.TextField(max_length=300, null=True, verbose_name='Текст отправки'),
        ),
    ]