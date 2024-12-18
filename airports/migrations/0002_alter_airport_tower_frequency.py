# Generated by Django 5.1.3 on 2024-11-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='tower_frequency',
            field=models.CharField(help_text='In MHz. If more than 1, separate by |, e.g. 131,5|879,5|987,5', max_length=100),
        ),
    ]
