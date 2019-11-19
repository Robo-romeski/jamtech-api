# Generated by Django 2.2.6 on 2019-11-19 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20191117_2138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businessprofile',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='businessprofile',
            name='summary',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='specialcredential',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='credentials', to='users.BusinessProfile'),
        ),
    ]
