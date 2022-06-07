# Generated by Django 3.2.4 on 2021-09-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210905_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='added_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='read',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='post',
            name='information_ru',
            field=models.TextField(verbose_name='Information (uz)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='information_uz',
            field=models.TextField(verbose_name='Information (uz)'),
        ),
    ]