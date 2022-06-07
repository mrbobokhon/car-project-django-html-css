# Generated by Django 3.2.4 on 2021-09-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210616_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='information_ru',
            field=models.TextField(verbose_name='Sarlavha (uz)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='information_uz',
            field=models.TextField(verbose_name='Sarlavha (uz)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Rasm'),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Sarlavha (uz)'),
        ),
        # migrations.AlterField(
        #     model_name='post',
        #     name='subject_uz',
        #     field=models.CharField(max_length=100, verbose_name='Sarlavha (uz)'),
        # ),
    ]