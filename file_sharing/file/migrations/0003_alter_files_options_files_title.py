# Generated by Django 4.2.5 on 2023-10-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_files'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'files'},
        ),
        migrations.AddField(
            model_name='files',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
