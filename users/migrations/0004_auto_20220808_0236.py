# Generated by Django 3.1.5 on 2022-08-08 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220808_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='City',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='Country',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='student',
            field=models.BooleanField(default='false'),
        ),
    ]
