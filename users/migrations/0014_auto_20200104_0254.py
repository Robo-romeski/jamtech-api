# Generated by Django 2.2.7 on 2020-01-04 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20191120_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessprofile',
            name='company_website',
            field=models.TextField(blank=True, null=True),
        ),
    ]
