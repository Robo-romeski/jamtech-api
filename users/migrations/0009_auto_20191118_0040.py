# Generated by Django 2.2.7 on 2019-11-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_merge_20191117_1946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessprofile',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='recent_projects',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='summary',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='work_seeking',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
