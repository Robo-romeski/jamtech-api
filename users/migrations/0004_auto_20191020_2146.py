# Generated by Django 2.2.6 on 2019-10-20 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_businessprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessprofile',
            name='special_credentials',
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='recent_project',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='work_seeking',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.CreateModel(
            name='SpecialCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.BusinessProfile')),
            ],
        ),
    ]
