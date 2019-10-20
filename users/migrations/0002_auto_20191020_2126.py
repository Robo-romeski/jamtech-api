# Generated by Django 2.2.6 on 2019-10-20 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('industry_category', models.CharField(blank=True, max_length=255)),
                ('industry_segment', models.CharField(blank=True, max_length=255)),
                ('experience_level', models.CharField(blank=True, max_length=255)),
                ('special_credentials', models.CharField(blank=True, max_length=255)),
                ('summary', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='employer',
            field=models.BooleanField(default=False),
        ),
    ]
