# Generated by Django 3.2.22 on 2024-05-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workrequest',
            name='Edate',
            field=models.CharField(default='NA', max_length=100),
        ),
        migrations.AddField(
            model_name='workrequest',
            name='Sdate',
            field=models.CharField(default='NA', max_length=100),
        ),
    ]
